import asyncpg
import asyncio
import logging

class Base:
  def __init__(self, user, password, host, port, database):
    self.user = user #Username
    self.password = password #Password
    self.host = host #Ipaddress
    self.port = port #Port default: 5432
    self.database = database #Database name
  
  #Creating a new pool. Use to create connection before using the class methods.
  async def create_pool(self):
    try:
      self.pool = await asyncpg.create_pool(
        user=self.user,
        password=self.password,
        host=self.host,
        port=self.port,
        database=self.database,
        min_size=1,
        max_size=10
      )
      await self.pool.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto;")
    except Exception as e:
      logger.error(f"Failed to create pool: {e}")
      raise e
    else:
      logger.info("Pool created successfully.")
  
  #Closing pools
  async def close_pool(self):
    try:
      await self.pool.close()
    except Exception as e:
      logger.error(f"Failed to close pool: {e}")
    else:
      logger.info("Pool closed successfully.")
  
  #Function to create a table.
  async def create_table(self, table_name, *columns):
    try:
      if not table_name: raise ValueError("Table name cannot be empty!")
      columns_str = ", ".join(columns)
      query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
      await self.pool.execute(query)
    except Exception as e:
      logger.error(f"Failed to create table: {e}")
    else:
      logger.info(f"Table '{table_name}' created successfully.")
      
  async def drop_table(self, table_name):
    try:
      if not table_name: raise ValueError("Table name cannot be empty!")
      await self.pool.execute("DROP TABLE {table_name}")
    except Exception as e:
      logger.error(f"Failed to drop table: {e}")
    else:
      logger.info(f"Table '{table_name}' dropped successfully.")
      
  async def insert_text(self, table_name, data):
    try:
      placeholders = []
      insert_names = data.keys()
      insert_names = ", ".join(insert_names)
      len_data = len(data)
      if len(data) == 0 or table_name == "": raise ValueError("Data cannot be empty!")
      if not table_name: raise ValueError("Table name cannot be empty!")
      for i in range(1, len_data+1):
        placeholders.append(f"${i}")
      insert_data_placeholders = ", ".join(placeholders)
      await self.pool.execute(f"INSERT INTO {table_name} ({insert_names}) VALUES ({insert_data_placeholders})", *data.values())
    except Exception as e:
      logger.error(f"Failed to insert data: {e}")
    else:
      logger.info("Data inserted successfully.")
