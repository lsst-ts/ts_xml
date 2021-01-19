<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <head><title>LSST SAL Commands</title></head>
  <body>
  <h2>SAL Commands</h2>
  <xsl:for-each select="SALCommandSet/SALCommand">
  <h3><xsl:value-of select="EFDB_Name"/> : 
<xsl:value-of select="Device"/>-<xsl:value-of select="Property"/>-<xsl:value-of select="Action"/>
  </h3>
  <table border="1">
  <xsl:for-each select="item">
    <xsl:if test="position()=1">
      <tr bgcolor="#9acd32"><th>Parameter</th><th>IDL Type</th><th>Count</th><th>Units</th></tr>
    </xsl:if>
     <tr>
      <td><xsl:value-of select="EFDB_Name"/></td>
      <td><xsl:value-of select="IDL_Type"/></td>
      <td><xsl:value-of select="Count"/></td>
      <td><xsl:value-of select="Units"/></td>
    </tr>
  </xsl:for-each>
  </table>
  </xsl:for-each>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>


