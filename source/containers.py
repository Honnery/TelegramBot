from dependency_injector import containers, providers

from databases.neo4j.neo4j_db import Neo4jApi
from messengers.telegram import telegram_wrappers


class Container(containers.DeclarativeContainer):
    messenger_config = providers.Configuration()
    database_config = providers.Configuration()
    messenger = providers.Factory(telegram_wrappers.TelegramApiWrapper,
                                  messenger_config.BOT_INFO.token
                                  )
    graph_api = providers.Factory(Neo4jApi,
                                  database_config.DATABASE_INFO.url,
                                  database_config.DATABASE_INFO.name,
                                  database_config.DATABASE_INFO.password)
