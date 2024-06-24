from abc import ABC

class BaseStorage(ABC):
  """Interface for file storage.
  """
  client = None

  def __init__(self, client = None):
    self.client = client
