from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingException,
                       QgsProcessingOutputNumber,
                       QgsProcessingParameterDistance,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterVectorDestination,
                       QgsProcessingParameterRasterDestination,
                       QgsVectorLayer)
from qgis import processing
from qgis.core import edit

class UnionCuencasHumedadEnCuencasProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer,
    creates some new layers and returns some results.
    """

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        # Must return a new copy of your algorithm.
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
                'INPUT',
                self.tr('Geometrías de cuencas'),
                types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        self.addParameter(
            QgsProcessingParameterFile(
                'TEXTFILE',
                self.tr('Datos de humedad en cuencas'),
                extension='csv'
            )
        )        
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                'OUTPUT',
                self.tr('Unión de geometrías de cuencas y datos de humedad en cuencas'),
            )
        )          

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """
        input_featuresource = self.parameterAsSource(parameters,
                                                     'INPUT',
                                                     context)
                                                     
        # Check for cancelation
        if feedback.isCanceled():
            return {}
          
        text_file_path = self.parameterAsString(parameters, 'TEXTFILE', context)
        
        #options = '?delimiter=%5Ct&detectTypes=yes'
        options = '?delimiter=,&detectTypes=yes'
        
        uri = 'file://{}{}'.format(text_file_path, options)
        
        vlayer = QgsVectorLayer(uri, 'tabla', 'delimitedtext')
        
        feedback.pushInfo('1')
        feedback.pushInfo(' '.join(vlayer.fields().names()))
        
        # Renombrar la segunda columna a "humedad"
        
        feedback.pushInfo('2')
        feedback.pushInfo(' '.join(vlayer.fields().names()))
             
        join_result = processing.run(
            'qgis:joinattributestable',
            {
               'INPUT': parameters['INPUT'],
               'FIELD': 'BASIN',
               'INPUT_2': vlayer,
               'FIELD_2': 'BASIN',
               'FIELDS_TO_COPY': '06ASM2024052006',
               'OUTPUT': parameters['OUTPUT'],
            },
            is_child_algorithm=True,
            context=context,
            feedback=feedback)

        if feedback.isCanceled():
            return {}

        # Return the results
        return {'OUTPUT': join_result['OUTPUT']}