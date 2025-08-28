 import logging
 import sqlalchemy
 import hashlib
 from flask import Blueprint, render_template, flash, redirect, request, session, url_for, escape
 def login():
     form = LoginForm()
     target = request.args.get("target")
     if target:
         logger.info("target: {}".format(target))
     if request.method == 'GET':