import logging as log

# LLamamos una configuracion basica del registro de eventos
# A partir de que nivel se muestra el mensaje
log.basicConfig(
    level=log.DEBUG,
    format="%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s",
    datefmt="%I:%M:%S %p",
    handlers=[log.FileHandler("capa_datos.log"), log.StreamHandler()],
)

# Obtener el logger
log = log.getLogger(__name__)