# Effigio
## Sistema de generación automática de enlaces de cámaras para emisión de eventos masivos en línea

Sistema creado para difusión de público masivo a través de OBS, Complu-OBS y HTML para la Universidad Complutense de Madrid.

# Versión I

Esta versión genera invitaciones push y view para compartir la cámara de los espectadores.

## Compilación en LaTeX

El sistema genera un PDF compulado con PDFLaTeX de forma local. Un documento por cada visitante que se quiera.

## Sistema de desplazamiento

Para evitar generar compilación de documentos repetidos si alguien nuevo necesita una invitación, se ha generado un comando de desplazamiento para que comience a generar invitaciones desde la última generada.

## Vistas en formato tabular

Después de generar las invitaciones se genera automáticamente un documento con todas las vistas por orden.

# Versión II

Esta versión se hizo para pruebas internas.

## OBS para 10 personas

La versión II permite generar un overlay estático para hasta 10 personas para OBS.

# Versión II

Versión funcional de Effigio para generación de eventos masivos.

## Overlay custom para infinitas personas

Sea cual sea el número, generará overlays de forma dinámica para importar con OBS.

## Balanceador de carga

Dado un número de visitantes, se generarán los overlays según las medidas más óptimas generadas con el balanceador de carga.

## Compilación de LaTeX mejorada

Se ha mejorado la compilación para reducir tiempos.
A saber, la versión 1 tardaba una media de 30 segundos para compilar 10 documentos, actualmente la versión 3 tarda 3 segundos en compilar 100 documentos.
