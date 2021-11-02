#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import os
from datetime import datetime
from os import path
from telepot.loop import MessageLoop
from time import sleep
import random
import calendar
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received:')
    print(msg)
    if command == '/start':
       chid = str(chat_id)
       pth = "/root/passwords/" + chid
       ch = path.exists(pth)
       global chd
       chd = "root/passwords/" + chid
       global havePSWD
       havePSWD = 0
       global year
       year = 0
       global month
       month = 0
       global finaldate
       finaldate = 0
       global _month
       _month = 0
       global monthA
       global currentMonth
       global intMonth
       global currentYear
       global currentDay
       global intYear
       montha = 0
       global day
       day = 0
       global hour
       hour = 0
       global finish
       finish = 0
       global _finish
       _finish = 0
       global chid
       global chPass
       global ch
       global msID
       markup = ReplyKeyboardMarkup(keyboard=[
                           ['Сгенерировать пароль'],['Сгенерировать PIN'],['Использовать свой']
                     
                   ], resize_keyboard=True)
       bot.sendMessage (chat_id, "Выберите действие", reply_markup=markup)
    elif command == u'Сгенерировать пароль':
         password = ''
         for x in range(8): #Количество символов (16)
          password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
          print (password)
         if ch:
          shortpth = "/root/passwords/"        
          os.chdir (shortpth)          
          os.chdir (chid)
          os.mkdir(password)
          os.chdir(password)
          havePSWD = 1
          markup = ReplyKeyboardMarkup(keyboard=[
                           ['Готово']
                     
                   ], resize_keyboard=True)
          #bot.sendMessage (chat_id, str(password + "\nСкопируйте этот пароль и установите его для Вашего приложения"), reply_markup=markup)
          msID = bot.sendMessage (chat_id, str(password))
          bot.sendMessage (chat_id, "Скопируйте этот пароль и установите его для Вашего приложения", reply_markup=markup)
          #print(msg)
         else:   
          
          shortpth = "/root/passwords/"
          os.chdir (shortpth)
          os.mkdir (chid)
          os.chdir (chid)
          os.mkdir(password)
          os.chdir(password)
          havePSWD = 1
          markup = ReplyKeyboardMarkup(keyboard=[
                           ['Готово']
                     
                   ], resize_keyboard=True)
          msID = bot.sendMessage (chat_id, str(password))
          bot.sendMessage (chat_id, "Скопируйте этот пароль и установите его для Вашего приложения", reply_markup=markup)
          #msID = telepot.message_identifier(msg)
    elif command == u'Сгенерировать PIN':
         password = ''
         for x in range(4): #Количество символов (16)
          password = password + random.choice(list('1234567890'))
          print (password)
         if ch:
          shortpth = "/root/passwords/"        
          os.chdir (shortpth)          
          os.chdir (chid)
          os.mkdir(password)
          os.chdir(password)
          havePSWD = 1
          markup = ReplyKeyboardMarkup(keyboard=[
                           ['Готово']
                     
                   ], resize_keyboard=True)
          msID = bot.sendMessage (chat_id, str(password))
          bot.sendMessage (chat_id, "Скопируйте этот PIN и установите его для Вашего приложения", reply_markup=markup)
          #msID = telepot.message_identifier(msg)
          #print(msID)
         else:   
          
          shortpth = "/root/passwords/"
          os.chdir (shortpth)
          os.mkdir (chid)
          os.chdir (chid)
          os.mkdir(password)
          os.chdir(password)
          havePSWD = 1
          markup = ReplyKeyboardMarkup(keyboard=[
                           ['Готово']
                     
                   ], resize_keyboard=True)
          msID = bot.sendMessage (chat_id, str(password))
          bot.sendMessage (chat_id, "Скопируйте этот PIN и установите его для Вашего приложения", reply_markup=markup)
    
    elif command == u'Использовать свой':    
       if ch:
        shortpth = "/root/passwords/"        
        os.chdir (shortpth)
        bot.sendMessage (chat_id, str("Отправьте пароль или PIN-код боту в сообщении"))
        os.chdir (chid) 
       else:   
        bot.sendMessage (chat_id, str("Отправьте пароль или PIN-код боту в сообщении"))
        shortpth = "/root/passwords/"
        os.chdir (shortpth)
        os.mkdir (chid)
        os.chdir (chid)
    elif command == u"Готово":
       bot.deleteMessage(telepot.message_identifier(msID))
       markup = ReplyKeyboardMarkup(keyboard=[
                           ['2021'],['2022'],['2023'],['2024'],['2025']
                     
                   ], resize_keyboard=True)
       bot.sendMessage (chat_id, "Пароль принят! Укажите год, в котором пароль будет возвращен", reply_markup=markup)    
    elif command != '/start' and havePSWD == 0 and finish != 1:
       print (command)
       upper_case = 0
       lower_case = 0
       number = 0

       for i in command:
         if i.isupper():
           upper_case += 1
         elif i.islower():
           lower_case += 1
         elif i.isdigit():
           number += 1    

       if len (command) <= 3:
             bot.sendMessage (chat_id, str("Пароль должен быть не короче 4 символов"))
       else:
          #global havePSWD
          pthPass = "/root/passwords/" + chid + "/" + command
          chPass = path.exists(pthPass)
          if chPass:
                bot.sendMessage (chat_id, str("Такой пароль уже принят, пожалуйста начните сначала и укажите другой"))
                markup = ReplyKeyboardMarkup(keyboard=[
                           ['/start']

                  ], resize_keyboard=True)
                bot.sendMessage (chat_id, str("/start"))
                havePSWD = 0
          else:        
                 os.mkdir(command)
                 os.chdir(command)
                 pthPass = "/root/passwords/" + chid + "/" + command
                 chPass = path.exists(pthPass)
                 if chPass:
                  havePSWD = 1
                  bot.deleteMessage(telepot.message_identifier(msg))
                  markup = ReplyKeyboardMarkup(keyboard=[
                           ['2021'],['2022'],['2023'],['2024'],['2025']
                     
                   ], resize_keyboard=True)
                  bot.sendMessage (chat_id, "Пароль принят! Укажите год, в котором пароль будет возвращен", reply_markup=markup)
                 else:
                      bot.sendMessage (chat_id, "Что-то пошло не так, пожалуйста попробуйте ввести другой пароль")
             
    elif command == "2021" or command == "2022" or command == "2023" or command == "2024" or command == "2025" and havePSWD == 1:
      #global year
      year = str(command)
      intYear = int(year)
      res = ""
      currentMonth = datetime.now().month
      currentYear = datetime.now().year
      currentYear = str(currentYear)
      if currentMonth == 1 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
              ['Январь'],['Февраль'],['Март'],['Апрель'],['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==2 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
              ['Февраль'],['Март'],['Апрель'],['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==3 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Март'],['Апрель'],['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==4 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Апрель'],['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==5 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==6 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==7 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==8 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==9 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==10 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==11 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Ноябрь'],['Декабрь']
             ], resize_keyboard=True)
      elif currentMonth ==12 and year == currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Декабрь']
             ], resize_keyboard=True)
      elif year != currentYear:
       markup = ReplyKeyboardMarkup(keyboard=[
               ['Январь'],['Февраль'],['Март'],['Апрель'],['Май'],['Июнь'],['Июль'],['Август'],['Сентябрь'],['Октябрь'],['Ноябрь'],['Декабрь']
             ], resize_keyboard=True, one_time_keyboard=True)
      bot.sendMessage (chat_id, "Укажите месяц", reply_markup=markup)
             
      
      
    elif year != 0 and _month == 0 and havePSWD == 1:
      month = command
      if month == u"Январь":
           _month = "1"
           monthA = "января"
      elif month == u"Февраль":
           _month = "2"
           monthA = "февраля"
      elif month == u"Март":
           _month = "3"
           monthA = "марта"
      elif month == u"Апрель":
           _month = "4"
           monthA = "апреля"
      elif month == u"Май":
           _month = "5"
           monthA = "мая"
      elif month == u"Июнь":
           _month = "6"
           monthA = "июня"
      elif month == u"Июль":
           _month = "7"
           monthA = "июля"
      elif month == u"Август":
           _month = "8"
           monthA = "августа"
      elif month == u"Сентябрь":
           _month = "9"
           monthA = "сентября"
      elif month == u"Октябрь":
           _month = "10"
           monthA = "октября"
      elif month == u"Ноябрь":
           _month = "11"
           monthA = "ноября"
      elif month == u"Декабрь":
           _month = "12"
           monthA = "декабря"
      currentMonth = datetime.now().month
      currentDay = datetime.now().day
      #print(currentMonth)
      intMonth = int(_month)
      currentDay = str(currentDay)
      currentYear = datetime.now().year

      e = (calendar.monthrange(intYear, intMonth)[1])
      if e == 30:
       
       #print (currentDay)


       if currentMonth == intMonth and currentDay == "1" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "2" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "3" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "4" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "5" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "6" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "7" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "8" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "9" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "10" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "11" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "12" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "13" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "14" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "15" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "16" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "17" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "18" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "19" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "20" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "21" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "22" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "23" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "24" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "25" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "26" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "27" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "28" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['28'],['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "29" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['29'],['30']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "30" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['30']
                 ], resize_keyboard=True)
       elif currentMonth != intMonth or intYear != currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30']
                 ], resize_keyboard=True)
      
       bot.sendMessage (chat_id, "Укажите день", reply_markup=markup)

      elif e == 31:
       if currentMonth == intMonth and currentDay == "1" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "2" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "3" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "4" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "5" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "6" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "7" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "8" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "9" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "10" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "11" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "12" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "13" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "14" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "15" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "16" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "17" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "18" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "19" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "20" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "21" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "22" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "23" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "24" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "25" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "26" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "27" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "28" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "29" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['29'],['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "30" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['30'],['31']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "31" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['31']
                 ], resize_keyboard=True)


       elif currentMonth != intMonth or intYear != currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28'],['29'],['30'],['31']
                 ], resize_keyboard=True)
      
       bot.sendMessage (chat_id, "Укажите день", reply_markup=markup)

      elif e == 28:
       #print (e)
       if currentMonth == intMonth and currentDay == "1" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "2" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "3" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "4" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "5" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "6" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "7" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "8" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "9" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "10" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "11" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "12" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "13" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "14" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "15" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "16" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "17" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "18" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "19" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "20" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "21" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "22" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "23" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "24" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "25" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "26" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['26'],['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "27" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['27'],['28']
                 ], resize_keyboard=True)
       elif currentMonth == intMonth and currentDay == "28" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['28']
                 ], resize_keyboard=True)
       
       elif currentMonth != intMonth or intYear != currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23'],['24'],['25'],['26'],['27'],['28']
                 ], resize_keyboard=True)
      
       bot.sendMessage (chat_id, "Укажите день", reply_markup=markup)

      
    elif _month != 0 and hour == 0 and finish != 1 and havePSWD == 1:
      day = str(command)
      currentHour = datetime.now().hour
      currentHour = str(currentHour)
      currentDay = datetime.now().day
      intDay = int(day)
      
      if intDay == currentDay and currentHour == "0" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "1" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "2" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "3" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "4" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "5" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "6" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "7" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "8" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "9" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "10" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "11" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "12" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "13" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "14" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "15" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                   ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "16" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "17" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "18" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "19" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "20" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['21'],['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "21" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['22'],['23']
                 ], resize_keyboard=True)
      elif intDay == currentDay and currentHour == "22" and intYear == currentYear:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['23']
                 ], resize_keyboard=True)
      elif intDay != currentDay or intYear != currentYear or currentMonth != intMonth:
              markup = ReplyKeyboardMarkup(keyboard=[
                   ['00'],['01'],['02'],['03'],['04'],['05'],['06'],['07'],['08'],['09'],['10'],['11'],['12'],['13'],['14'],['15'],['16'],['17'],['18'],['19'],['20'],['21'],['22'],['23']
                 ], resize_keyboard=True)
                

      bot.sendMessage (chat_id, "Укажите час", reply_markup=markup)
      finish = 1

    elif command != '/start' and finish == 1:
      hour = str(command)
      finaldate = str(year + _month + day + hour + "00")
      chat_id = str(chat_id)
      #command = str(command)
      #current_datetime = datetime.now()
      #curr_Date = (current_datetime.year,current_datetime.month,current_datetime.day,current_datetime.hour,current_datetime.minute)
      #curr_Date = str(curr_Date)
      #curr_Date = curr_Date.replace(", ", "")
      finalMessage = "Дата принята. Ваш chat_ID: " + chat_id + ". Бот вышлет пароль в " + year + " году, " + day + " " + monthA + ", в " + hour + " часов"
      bot.sendMessage (chat_id, str(finalMessage))
      os.mkdir(finaldate)
      markup = ReplyKeyboardMarkup(keyboard=[
                     ['/start']

             ], resize_keyboard=True)

      bot.sendMessage (chat_id, "/start", reply_markup=markup)
      

bot = telepot.Bot('2070210645:AAEtex17pVoN64_fD8oNljIDFoSeQv-51KA')

MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)

