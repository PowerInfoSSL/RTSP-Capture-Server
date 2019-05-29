import os,sys, cv2, threading as thr
import numpy as np
from time import sleep
opencv_name = []
picture_number = 0

# First Initialization
path = os.getcwd()


def firs_i():
    cam_lst = []
    try:
        total_cam=int(input('Pleas Enter number of camera:'))
    except:
        print('you must enter a number\n\n Script Exit soon')
        exit()
    for i in range(total_cam):
        cam=input("Camera number %s\n\n Pleas Enter RTSP URL:\n" %i)
        if cam is not "":
            cam_lst.append(cam)
    co=input("\n\n\nyou entred %s Camera for Monitoring if its correct, then type 'yes' to continue or pressess Enter to Exit.\n:" % str(total_cam))
    if co=='yes' or co=='Yes' or co=='YES':
        for i in cam_lst: print(i)
    else:
        exit()
    #write CAM-LIST to a file:
    cam_file=open("camfile.txt",'w+')
    for i in cam_lst:
        cam_file.writelines(i + '\n')
        print("\n[+]New Cam Setting Saved.[\n]%s\n\n" % i)
    cam_file.close()
    print("Initialization was finished successfully.\n" )
    input('Press Enter to continue...\n')


#------------------------------------------------CHeck Already Initialized or not ---------------------------------
if os.path.isfile('camfile.txt') !=True:
    firs_i()

#*********************************************** Main Defination for RTSP view *********************************************************
#---------------------------------------------------------------------------------------------------------------------------------------
#*********************************************** Main Defination for RTSP view *********************************************************
#---------------------------------------------------------------------------------------------------------------------------------------
#*********************************************** Main Defination for RTSP view *********************************************************
#---------------------------------------------------------------------------------------------------------------------------------------
def view_cam(rtsp_lst,title,x=100,y=100):
    vid1,vid2,vid3,vid4,vid5=cv2.VideoCapture(''),cv2.VideoCapture(''),cv2.VideoCapture(''),cv2.VideoCapture(''),cv2.VideoCapture('')
    last_frame=[]
    p=0
    #Read and Capture Streams
    for i in rtsp_lst:
        print('\nNew Camera Initialization....' )
        sleep(1)
        if 'rtsp' in i:
            if p==0:
                vid1=cv2.VideoCapture(i)
            if p==1:
                vid2=cv2.VideoCapture(i)
            if p==2:
                vid3=cv2.VideoCapture(i)
            if p==3:
                vid4=cv2.VideoCapture(i)
            if p==4:
                vid5=cv2.VideoCapture(i)
            p +=1
    #---------------------Refreash Frames ----------------------
    while 1:
        if vid1.isOpened():
            chk,frm=vid1.read()
            if chk ==True:
                last_frame.append(cv2.resize(frm,(x,y)))
        if vid2.isOpened():
            chk,frm=vid2.read()
            if chk ==True:
                last_frame.append(cv2.resize(frm,(x,y)))
        if vid3.isOpened():
            chk,frm=vid3.read()
            if chk ==True:
                last_frame.append(cv2.resize(frm,(x,y)))
        #-----------VID4
        if vid4.isOpened():
            chk,frm=vid4.read()
            if chk ==True:
                last_frame.append(cv2.resize(frm,(x,y)))
        #------------VID5
        if vid5.isOpened():
            chk,frm=vid5.read()
            if chk ==True:
                last_frame.append(cv2.resize(frm,(x,y)))
        # *************************************************                                      *********************
        # *************************************************                                      *********************
        # *************************************************                                      *********************
        #****************************************************END of refresh all 5 item video show*********************
        # *************************************************                                      *********************
        # *************************************************                                      *********************
        # *************************************************                                      *********************
        #                                                         Single view Definition with number
        def single_view(cn):
            #****************************************************************
            #******************* Destroy each window created ****************
            # ****************************************************************
            #
            def wr_img(f_name,frame):
                #
                global picture_number
                picture_number += 1
                cv2.imwrite('capture\\%s.jpg' % picture_number, frame)
            if cn ==ord('1'):
                cv2.destroyAllWindows()
                while 1:
                    if vid1.isOpened():
                        chk1,frm1=vid1.read()
                        if chk1==True:
                            cv2.imshow('Camera-1',frm1)
                            key=cv2.waitKey(1)
                            if key==27:
                                cv2.destroyWindow('Camera-1')
                                #main_exec()
                                break
                            if key==ord('c'):
                                wr_img('Camera1-%s'%picture_number,frm1)
            if cn ==ord('2'):
                cv2.destroyAllWindows()
                while 1:
                    if vid2.isOpened():
                        chk,frm = vid2.read()
                        if chk == True:
                            cv2.imshow('Camera-2', frm)
                            key = cv2.waitKey(1)
                            if key == 27:
                                cv2.destroyWindow('Camera-2')
                                # main_exec()
                                break
                            if key == ord('c'):
                                wr_img('Camera2-%s'%picture_number, frm)
            if cn == ord('3'):
                cv2.destroyAllWindows()
                while 1:
                    if vid3.isOpened():
                        chk, frm=vid3.read()
                        if chk == True:
                            cv2.imshow('Camera-3', frm)
                            key=cv2.waitKey(1)
                            if key == 27:
                                cv2.destroyWindow('Camera-3')
                                # main_exec()
                                break
                            if key == ord('c'):
                                wr_img('Camera3-%s'%picture_number,frm)
            if cn == ord('4'):
                cv2.destroyAllWindows()
                while 1:
                    if vid4.isOpened():
                        chk, frm = vid4.read()
                        if chk == True:
                            cv2.imshow('Camera-4', frm)
                            key=cv2.waitKey(1)
                            if key == 27:
                                cv2.destroyWindow('Camera-4')
                                # main_exec()
                                break
                            if key==ord('c'):
                                wr_img('Camera4-%s'%picture_number,frm)
            if cn ==ord('5'):
                cv2.destroyAllWindows()
                while 1:
                    if vid5.isOpened():
                        chk,frm=vid5.read()
                        if chk==True:
                            cv2.imshow('Camera-5',frm)
                            key=cv2.waitKey(1)
                            if key==27:
                                #exit()
                                cv2.destroyWindow('Camera-5')
                                #main_exec()
                                break
                            if key==ord('c'):
                                wr_img('Camera5-%s'%picture_number,frm)
        #--------Create Merge frame
        frame_np=np.concatenate(last_frame,axis=1)
        cv2.imshow(title,frame_np)
        last_frame=[]
        key=cv2.waitKey(1)
        if key == 27:
            cv2.destroyWindow(title)
            quit()
        single_view(key)


    #*************///////////////////\\\\\\\\\\\\\\\\    END of Main defination **********************************


def main_exec():
    #
    #
    # ----------Read stream address from file
    # ------------------------------------------Check file exist
    if os.path.isfile('camfile.txt') == False:
        quit()
        #
        #
    file_cam = open('camfile.txt', 'r')
    list_camfile = file_cam.readlines()
    lst_camf_no_ent = []
    for i in list_camfile:
        lst_camf_no_ent.append(i.split('\n')[0])



    # -----------Split 5 item for send to show list and START IT.
    #***********************************************************************************///////////\\\\\\\


    five_item = []
    #
    cam_num = 0
    gr_num = 0
    for i in lst_camf_no_ent:
        gr_num += 1
        if len(five_item) < 5:
            five_item.append(i)
            #
        if len(five_item) == 5:
            tr_view = thr.Thread(target=view_cam, args=(five_item,'CamGR%s' %cam_num, ), name='Group-%s' % gr_num)
            tr_view.start()
            # view_cam(five_item)
            five_item = []
            cam_num += 1
            continue


        #
        #
        #


        if cam_num+1 == len(lst_camf_no_ent):
            #
            gr_num += 1
            tr_view = thr.Thread(target=view_cam, args=(five_item, 'Camera Groupw %s' % gr_num, ))
            tr_view.start()
        cam_num += 1


main_exec()
