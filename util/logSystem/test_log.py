import log_manager

log_writer = log_manager.Log_manager()
log_writer.info(message="этот текст белый")
log_writer.errors(message="этот текст красный")