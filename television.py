class Television
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self):
    self.__status = False
    self.__muted = False
    self.__volume = Television.MIN_VOLUME
    self.__channel = Television.MIN_CHANNEL

  def power(self):
    if self.__status == False: 
      self.__status == True
    else:
      self.__status == False

  def mute(self):
    if self.__muted == False: 
      self.__muted == True
    else:
      self.__muted == False

  def channel_up(self):
    if self.__status == True:
      if self.__channel < Television.__MAX_CHANNEL:
        self.__channel += 1
      else:
        self.__channel == Television.__MIN_CHANNEL

  def channel_down(self):
    if self.__status == True:
      if self.__channel > Television.__MIN_CHANNEL:
        self.__channel -= 1
      else:
        self.__channel == Television.__MAX_CHANNEL
        
  def volume_up(self):
    if self.__status == True:
      self.__muted == False
      if self.__volume < Television.__MAX_VOLUME:
        self.__volume += 1

  def volume_down(self):
    if self.__status == True:
      if self.__volume > Television.__MIN_VOLUME:
        self.__volume -= 1
      else:
        self.__muted == True

  def __str__(self):
    if self.__muted == True:
      return f'Volume = {Television.__MIN_VOLUME}'
    else:
      return f'Volume = {self.__volume}'
