<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" hasScaleBasedVisibilityFlag="0" styleCategories="AllStyleCategories" version="3.24.2-Tisler" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal fetchMode="0" enabled="0" mode="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <Option type="Map">
      <Option type="bool" value="false" name="WMSBackgroundLayer"/>
      <Option type="bool" value="false" name="WMSPublishDataSourceUrl"/>
      <Option type="int" value="0" name="embeddedWidgets/count"/>
      <Option type="QString" value="Value" name="identify/format"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" value="" name="name"/>
      <Option name="properties"/>
      <Option type="QString" value="collection" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" enabled="false" zoomedOutResamplingMethod="nearestNeighbour" maxOversampling="2"/>
    </provider>
    <rasterrenderer type="paletted" band="1" opacity="1" nodataColor="" alphaBand="-1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
        <paletteEntry alpha="255" value="1" color="#1a9641" label="1"/>
        <paletteEntry alpha="255" value="2" color="#8acc62" label="2"/>
        <paletteEntry alpha="255" value="3" color="#dcf09e" label="3"/>
        <paletteEntry alpha="255" value="4" color="#ffdf9a" label="4"/>
        <paletteEntry alpha="255" value="5" color="#f69053" label="5"/>
        <paletteEntry alpha="255" value="6" color="#d7191c" label="6"/>
      </colorPalette>
      <colorramp type="gradient" name="[source]">
        <Option type="Map">
          <Option type="QString" value="26,150,65,255" name="color1"/>
          <Option type="QString" value="215,25,28,255" name="color2"/>
          <Option type="QString" value="cw" name="direction"/>
          <Option type="QString" value="0" name="discrete"/>
          <Option type="QString" value="gradient" name="rampType"/>
          <Option type="QString" value="rgb" name="spec"/>
          <Option type="QString" value="0.25;166,217,106,255;rgb;cw:0.5;255,255,192,255;rgb;cw:0.75;253,174,97,255;rgb;cw" name="stops"/>
        </Option>
        <prop v="26,150,65,255" k="color1"/>
        <prop v="215,25,28,255" k="color2"/>
        <prop v="cw" k="direction"/>
        <prop v="0" k="discrete"/>
        <prop v="gradient" k="rampType"/>
        <prop v="rgb" k="spec"/>
        <prop v="0.25;166,217,106,255;rgb;cw:0.5;255,255,192,255;rgb;cw:0.75;253,174,97,255;rgb;cw" k="stops"/>
      </colorramp>
    </rasterrenderer>
    <brightnesscontrast contrast="0" gamma="1" brightness="0"/>
    <huesaturation grayscaleMode="0" invertColors="0" saturation="0" colorizeRed="255" colorizeGreen="128" colorizeOn="0" colorizeBlue="128" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
