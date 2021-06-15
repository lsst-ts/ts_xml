<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="/">
    <html>
      <head>
        <title>LSST SAL Telemetry</title>
        <link rel="stylesheet" href="../../ts_xml/schema/SALTelemetrySet.css" type="text/css"/>
      </head>
      <body>
        <h2>SAL Telemetry</h2>
        <xsl:for-each select="SALTelemetrySet/SALTelemetry">
          <h3>
            <xsl:value-of select="EFDB_Topic"/>
          </h3>
          <table>
            <xsl:for-each select="item">
              <xsl:if test="position()=1">
                <tr class="header">
                  <th>Name</th>
                  <th>IDL Type</th>
                  <th>Count</th>
                  <th>Units</th>
                </tr>
              </xsl:if>
              <tr>
                <td>
                  <xsl:value-of select="EFDB_Name"/>
                </td>
                <td>
                  <xsl:value-of select="IDL_Type"/>
                </td>
                <td>
                  <xsl:value-of select="Count"/>
                </td>
                <td>
                  <xsl:value-of select="Units"/>
                </td>
              </tr>
            </xsl:for-each>
          </table>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
