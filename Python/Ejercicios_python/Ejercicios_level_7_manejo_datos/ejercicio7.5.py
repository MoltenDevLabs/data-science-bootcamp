# Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea (url: https://ec.europa.eu/eurostat/estat-nav-tree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de un país y muestre el PIB per cápita de ese país do todos los años disponibles.

def abrir_fichero(p):
  with open("https://ec.europa.eu/eurostat/estat-nav-tree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true", "r", encoding="utf-8") as f:



p = input("Pon las iniciales de un país: ").lower()


