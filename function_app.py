import azure.functions as func
import logging

app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="voyageretl/mck-birdeye/ExportedFiles",
                               connection="voyageretl_STORAGE") 
def CreateCommonCustomTablesCompatibleCSV(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
