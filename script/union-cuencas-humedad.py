from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsFeature,
                       QgsField,
                       QgsFields,
                       QgsVectorLayer,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFeatureSink)
from qgis import processing


class UnionCuencasHumedadEnCuencasProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    Este algoritmo realiza una unión (join) de las geometrías de una capa vectorial
    de cuencas hidrográficas y un archivo de texto con datos de humedad de las cuencas.
      - La capa de cuencas debe tener la columna: 'BASIN' (código de la cuenca)
      - El archivo de texto debe estar separado por tabuladores y tener dos columnas:
        'BASIN' y una columna numérica (con cualquier nombre) con el dato de humedad.
      - La capa de salida tendrá las columnas: 'BASIN' y 'HUMEDAD'
    """
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'
    TEXTFILE = 'TEXTFILE'
    

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return UnionCuencasHumedadEnCuencasProcessingAlgorithm()

    def name(self):
        """
        Returns the unique algorithm name.
        """
        return 'uniongeometriascuencasdatoshumedadcuencas'

    def displayName(self):
        """
        Returns the translated algorithm name.
        """
        return self.tr('Unión de geometrías de cuencas y datos de humedad en cuencas')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to.
        """
        return self.tr('Modelo de inestabilidad de laderas')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs
        to.
        """
        return 'modeloinestabilidadladeras'

    def shortHelpString(self):
        """
        Returns a localised short help string for the algorithm.
        """
        return self.tr('Unión de geometrías de cuencas y datos de humedad en cuencas')

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and outputs of the algorithm.
        """
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Geometrías de cuencas'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                self.TEXTFILE,
                self.tr('Datos de humedad en cuencas'),
                extension='txt'
            )
        )        
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Unión'),
            )
        )          

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )
        text_file_path = self.parameterAsString(
            parameters,
            self.TEXTFILE,
            context
        )
                                                     
        # Check for cancelation
        if feedback.isCanceled():
            return {}
            
            
        # Impresión de la ruta original del archivo de texto
        feedback.pushInfo(text_file_path)
        
        # Reemplazo de barras invertidas por barras
        text_file_path = text_file_path.replace("\\", "/")
        # Impresión de la ruta modificada del archivo de texto
        feedback.pushInfo(text_file_path)
        
        # Opciones para procesamiento del archivo de texto
        options = '?delimiter=%5Ct&detectTypes=yes' # delimitador = tabulador
        # options = '?delimiter=,&detectTypes=yes' # delimitador = coma
        
        uri = 'file:///{}{}'.format(text_file_path, options)
        
        vlayer = QgsVectorLayer(uri, 'datos_humedad_cuencas', 'delimitedtext')
        if not vlayer.isValid():
            raise QgsProcessingException(self.tr('La capa generada por el archivo de texto es no es válida.'))
                   
        feedback.pushInfo('Columnas del archivo de texto: {}'.format(vlayer.fields().names()))
        
        # Configuración del archivo de salida (sink)
        fields = QgsFields()
        fields.append(QgsField('BASIN', QVariant.String))
        fields.append(QgsField('HUMEDAD', QVariant.Double))
        
        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context, fields, source.wkbType(), source.sourceCrs())
                   
        # Unión de los conjuntos de datos
        joined_layer = processing.run(
            'qgis:joinattributestable',
            {
               'INPUT': parameters[self.INPUT],
               'FIELD': 'BASIN',
               'INPUT_2': vlayer,
               'FIELD_2': 'BASIN',
               'FIELDS_TO_COPY': '', # se incluyen las dos columnas del archivo de texto
               'OUTPUT': 'memory:'
            },
            context=context,
            feedback=feedback)['OUTPUT']

        if feedback.isCanceled():
            return {}
            
        feedback.pushInfo('Columnas de la capa de unión: {}'.format(joined_layer.fields().names()))

        # Se recorre la capa de unión y se crean los registros de la salida
        for f in joined_layer.getFeatures():
            new_feature =  QgsFeature()
            # Set geometry to dissolved geometry
            new_feature.setGeometry(f.geometry())
            # Set attributes
            new_feature.setAttributes([f['BASIN'], f[2]]) # el dato de humedad debe estar en la tercera columna de la capa de unión
            sink.addFeature(new_feature, QgsFeatureSink.FastInsert)        
        
        
        return {self.OUTPUT: dest_id}