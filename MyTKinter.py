import os, sys, re, time
from inspect import currentframe, getframeinfo
from selenium.webdriver.remote.webelement import WebElement
from abc import ABCMeta, abstractmethod
import tkinter as tk
import tkinter.ttk as ttk


class ComboBoxTemplete(metaclass=ABCMeta):

  def __init__(self, title="", text="", **kwargs):
    """Generate a pop-up window for special messages."""
    self.obj = kwargs['obj']
    self.root = tk.Tk()
    self.root.title(title)
    w = 500     # popup window width
    h = 330     # popup window height
    sw = self.root.winfo_screenwidth()
    sh = self.root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    frameLabel1 = tk.Frame( self.root, padx=20, pady=20)
    frameLabel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
    frameLabel2 = tk.Frame( self.root, padx=20, pady=20 )
    frameLabel2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)
    w = tk.Text( frameLabel1, width=10, height=10, wrap='word', font='Arial 12 bold' )
    # text = re.sub('^[ ]{1,}', '', f"""
    #       집합건물의 동정보를 확인하시고, 열람을 원하시는 부동산의 선택버튼을 눌러주십시요.\r\n
    #       정부24의 조회결과 해당 집합건물의 동정보와 지번이 모두 동일할 수 있습니다.\r\n
    #       하나씩 선택해서 건물(동)명칭이 조회하시고, 조회되는 결과를 확인하시면서 진행해주세요.""".strip(), flags=re.MULTILINE)
    w.insert( 1.0, text )
    w.pack(fill = tk.BOTH, expand = tk.YES)
    # - have selection background appear like it does when the widget is activated (Tkinter 8.5+)
    # - have label background color match its parent background color via .cget('background')
    # - set relief='flat' to hide Text control borders
    # - set state='normal' to changes to text (while still allowing selection/clipboard copy)
    w.configure( bg=self.root.cget('bg'), relief='flat', state='normal' )
    combo = ttk.Combobox(frameLabel1, width=60, justify='left', font='Arial 12 bold')
    # 정확한부동산소재지번리스트
    combo['values'] = kwargs['values']
    self.comboSeleniumElements = kwargs['elements']
    combo.configure(state='readonly')
    combo.current(0)
    self.comboboxValue=combo.get()

    def click_item(event):
      self.comboboxValue = combo.get()

    combo.bind("<<ComboboxSelected>>", click_item)
    combo.pack()
    
    def pressed():
      self.pressed()

    self.b = tk.Button(frameLabel2, text="선택", bg='black', fg='white', command=pressed, width=20)
    self.b.pack(fill = tk.Y, expand = tk.YES)

    # The following three commands are needed so the window pops up on top on Windows...
    self.root.iconify()
    self.root.update()
    self.root.deiconify()
    self.root.mainloop()

  @abstractmethod
  def pressed(self):
    if self.comboboxValue is not None:
      print(f'ComboboxSelected : {self.comboboxValue}................')
      element: WebElement = self.comboSeleniumElements[self.comboboxValue]
      element.click()
      print(f'Combobox Destory Event 발생 root.destroy()...................')


class GovKrAlert:

  def __init__(self, title="", text=""):
      """Generate a pop-up window for special messages."""
      self.window_width, self.window_height = 0, 0
      self.root = tk.Tk()
      self.root.title(title)

      # 윈도우를 화면 가운데 보여지게 한다.
      w = 1024     # popup window width
      h = 350     # popup window height
      sw = self.root.winfo_screenwidth()
      sh = self.root.winfo_screenheight()
      x = (sw - w)/2
      y = (sh - h)/2
      self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

      self.frameLabel1 = tk.Frame( self.root, padx=20, pady=20)
      self.frameLabel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
      self.frameLabel2 = tk.Frame( self.root, padx=20, pady=20 )
      self.frameLabel2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

      # self.textF = tk.StringVar()
      self.w1 = tk.Text( self.frameLabel1, width=10, height=10, wrap='word', font=('Arial', 12, 'bold'))
      self.w1.insert( tk.CURRENT, text )
      self.w1.pack(side=tk.TOP, fill = tk.X, expand = tk.YES)
      
      self.w1.configure( bg=self.root.cget('bg'), relief='flat', state='normal' )
      self.b = tk.Button(self.frameLabel2, text="확인", bg='black', fg='white', command=self.root.destroy, width=20)
      self.b.pack(fill = tk.Y, expand = tk.YES)

      # The following three commands are needed so the window pops up on top on Windows...
      self.root.iconify()
      self.root.update()
      self.root.deiconify()
      
      self.root.mainloop()


class GovKrAlert_OK_EXIT:

  def __init__(self, 로그정보, title="", text=""):
      """Generate a pop-up window for special messages."""
      self.로그정보 = 로그정보
      self.window_width, self.window_height = 0, 0
      self.root = tk.Tk()
      self.root.title(title)
      
      # 윈도우를 화면 가운데 보여지게 한다.
      w = 1024     # popup window width
      h = 350     # popup window height
      sw = self.root.winfo_screenwidth()
      sh = self.root.winfo_screenheight()
      x = (sw - w)/2
      y = (sh - h)/2
      self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
      
      self.frameLabel1 = tk.Frame( self.root, padx=20, pady=20)
      self.frameLabel1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
      self.frameLabel2 = tk.Frame( self.root, padx=20, pady=20 )
      self.frameLabel2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.YES)

      self.w1 = tk.Text( self.frameLabel1, width=10, height=10, wrap='word', font=('Arial', 12, 'bold'))
      self.w1.insert( tk.CURRENT, text )
      self.w1.pack(side=tk.TOP, fill = tk.X, expand = tk.YES)
      
      self.w1.configure( bg=self.root.cget('bg'), relief='flat', state='normal' )
      self.b = tk.Button(self.frameLabel2, text="확인", bg='black', fg='white', command=self.root.destroy, width=20)
      self.b.pack(side=tk.LEFT, fill = tk.Y, expand = tk.YES)
      self.b = tk.Button(self.frameLabel2, text="종료", bg='black', fg='white', command=self.exit, width=20)
      self.b.pack(side=tk.RIGHT, fill = tk.Y, expand = tk.YES)

      # The following three commands are needed so the window pops up on top on Windows...
      self.root.iconify()
      self.root.update()
      self.root.deiconify()
      
      self.root.mainloop()

  def exit(self):
    self.root.destroy()
    print('종료 버튼을 눌렀습니다.........')
    print('프로그램을 종료합니다.........')
    sys.exit()

if __name__ == '__main__':

  text = re.sub('^[ ]{1,}', '', f"""
  파이썬 TK Window 팝업 테스트입니다.\r\n
  '확인' 버튼을 누르시면 팝업창이 닫히고, '종료' 버튼을 누르시면 프로그램이 종료됩니다.""".strip(), flags=re.MULTILINE)
  # GovKrAlert_OK_EXIT(None, "Python TK Window 테스트", text)
  GovKrAlert_OK_EXIT(None, "권한부족 오류", text)
  print('확인을 눌렀습니다. 윈도우창이 닫힙니다.........')
  print('3초 후에 프로그램이 닫힙니다.........')
  time.sleep(3)
  print('프로그램을 종료합니다.........')
  sys.exit()
