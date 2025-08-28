 from dependency_injector import containers, providers
 
from ..settings import get_settings
 from .persistence_container import PersistenceContainer
 from .publisher_container import PublisherContainer
 
     )
 
     # Configuration
    config = providers.Configuration(default=get_settings())
 
     # Persistence
     persistence_container: providers.Singleton[PersistenceContainer] = (