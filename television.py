class Television
"""
Class to represent television object.
Instance variable are not to be changed
"""
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self) -> None:
    """
    Method to initialize television object and create parameters
    """
    self.__status = False
    self.__muted = False
    self.__volume = Television.MIN_VOLUME
    self.__channel = Television.MIN_CHANNEL

  def power(self) -> None:
    """
    Method to set status to True or False depending on its active mode
    """
    if self.__status == False: 
      self.__status == True
    else:
      self.__status == False

  def mute(self) -> None:
    """
    Method to set muted variable to on or off dpending on active mode
    """
    if self.__muted == False: 
      self.__muted == True
    else:
      self.__muted == False

  def channel_up(self) -> None:
    """
    Method to increase channel by one unless at maximum, then cycles back to minimum
    """
    if self.__status == True:
      if self.__channel < Television.__MAX_CHANNEL:
        self.__channel += 1
      else:
        self.__channel == Television.__MIN_CHANNEL

  def channel_down(self) -> None:
    """
    Opposite of channel_up, decreases channel by one unless at minimum, then returns to maximum
    """
    if self.__status == True:
      if self.__channel > Television.__MIN_CHANNEL:
        self.__channel -= 1
      else:
        self.__channel == Television.__MAX_CHANNEL
        
  def volume_up(self -> None:
    """
    Method to increase volume by one unless already at maximum, then no change
    """
    if self.__status == True:
      self.__muted == False
      if self.__volume < Television.__MAX_VOLUME:
        self.__volume += 1

  def volume_down(self) -> None:
    """
    Decreases volume by one unless at minimum, then no change
    """
    if self.__status == True:
      if self.__volume > Television.__MIN_VOLUME:
        self.__volume -= 1
      else:
        self.__muted == True

  def __str__(self) -> str:
    """
    Prints out the volume the television is at with special condition for if volume is muted
    """
    if self.__muted == True:
      return f'Volume = {Television.__MIN_VOLUME}'
    else:
      return f'Volume = {self.__volume}'
