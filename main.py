from src.orm import SyncOrm

sync = SyncOrm()
sync.create_table()
sync.insert_workers()
sync.select_workers()
sync.update_worker()
sync.select_workers()

