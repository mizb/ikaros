# -*- coding: utf-8 -*-
import os
import re
import errno
import shutil
from .log import log

video_type = ['.mp4', '.avi', '.rmvb', '.wmv',
              '.mov', '.mkv', '.flv', '.ts', '.webm', '.iso']
ext_type = ['.ass', '.srt', '.sub', '.ssa', '.smi', '.idx', '.sup',
            '.psb', '.usf', '.xss', '.ssf', '.rt', '.lrc', '.sbv', '.vtt', '.ttml']

video_filter = ['*.mp4', '*.avi', '*.rmvb', '*.wmv',
                '*.mov', '*.mkv', '*.flv', '*.ts', '*.webm', '*.iso']
ext_filter = ['*.ass', '*.srt', '*.sub', '*.ssa', '*.smi', '*.idx', '*.sup',
              '*.psb', '*.usf', '*.xss', '*.ssf', '*.rt', '*.lrc', '*.sbv', '*.vtt', '*.ttml']


def CreatFolder(foldername):
    """ 创建文件
    """
    if not os.path.exists(foldername + '/'):
        try:
            os.makedirs(foldername + '/')
        except Exception as e:
            log.info("[-]failed!can not be make Failed output folder\n[-](Please run as Administrator)")
            log.error(e)
            return


def CleanFolder(foldername):
    """ rm and create folder
    """
    try:
        shutil.rmtree(foldername)
    except:
        pass
    CreatFolder(foldername)


def cleanfilebysuffix(folder, suffix):
    """ 清理指定目录下所有匹配格式文件
    """
    dirs = os.listdir(folder)
    for file in dirs:
        f = os.path.join(folder, file)
        if os.path.isdir(f):
            cleanfilebysuffix(f, suffix)
        elif os.path.splitext(f)[1].lower() in suffix:
            log.info("clean file by suffix [{}]".format(f))
            os.remove(f)


def cleanfolderwithoutsuffix(folder, suffix):
    """ 清理目录下无匹配文件的目录
    """
    hassuffix = False
    dirs = os.listdir(folder)
    for file in dirs:
        f = os.path.join(folder, file)
        if os.path.isdir(f):
            hastag = cleanfolderwithoutsuffix(f, suffix)
            if hastag:
                hassuffix = True
            else:
                log.info("clean empty media folder [{}]".format(f))
                shutil.rmtree(f)
        elif os.path.splitext(f)[1].lower() in suffix:
            hassuffix = True
    return hassuffix


def cleanfolderbyfilter(folder, filter):
    """ clean folder by filter
    
    if all files removed, rm folder
    """
    cleanAll = True
    dirs = os.listdir(folder)
    for file in dirs:
        f = os.path.join(folder, file)
        if os.path.isdir(f):
            cleanAll = False
        else:
            if filter in file:
                log.info("clean folder by filter [{}]".format(f))
                os.remove(f)
            else:
                cleanAll = False
    if cleanAll:
        shutil.rmtree(folder)


def cleanscrapingfile(folder, filter):
    """ clean scraping file
    """
    filters = [filter + '.', filter + '-fanart.', filter + '-poster.', filter + '-thumb.']

    dirs = os.listdir(folder)
    for file in dirs:
        f = os.path.join(folder, file)
        if not os.path.isdir(f):
            for s in filters:
                if s in file:
                    log.info("clean scraping file [{}]".format(f))
                    os.remove(f)


def symlink_force(srcpath, dstpath):
    """ create symlink
    https://stackoverflow.com/questions/8299386/modifying-a-symlink-in-python
    """
    try:
        os.symlink(srcpath, dstpath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(dstpath)
            os.symlink(srcpath, dstpath)
        else:
            raise e


def hardlink_force(srcpath, dstpath):
    """ create hard link
    """
    try:
        os.link(srcpath, dstpath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            os.remove(dstpath)
            os.link(srcpath, dstpath)
        else:
            raise e


def replace_CJK(base: str):
    """ try to replace CJK or brackets

    eg: 你好  [4k修复] (实例1)
    """
    tmp = base
    for n in re.findall(r'[\(\[\（](.*?)[\)\]\）]', base):
        if re.findall(r'[\u4e00-\u9fff]+', n):
            cop = re.compile("[\(\[\（]" + n + "[\)\]\）]")
            tmp = cop.sub('', tmp)
    tmp = re.sub(r'[\u4e00-\u9fff]+', '', tmp)
    return tmp
