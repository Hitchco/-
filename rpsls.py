#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    if name=="ʯͷ":
        a=0
    elif name=="ʷ����":
        a=1
    elif name=="ֽ":
        a=2
    elif name=="����":
        a=3
    elif name=="����":
        a=4
    else:
        print("Error: No Correct Name")
    return a






    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


     #��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
    if number==0:
        b="ʯͷ"
    elif number==1:
        b="ʷ����"
    elif number==2:
        b="ֽ"
    elif number==3:
        b="����"
    elif number==4:
        b="����"
    return b

    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    #��дִ�д���,������ɺ�passɾ��


def rpsls(choice_name):
    player_choice_number = name_to_number(choice_name)
    comp_number = random.randrange(0, 4)
    comp_choice=number_to_name(comp_number)

    print("�������ѡ��Ϊ��"+comp_choice)
    if player_choice_number>comp_number:
        distance=player_choice_number-comp_number
    else:
        distance = player_choice_number - comp_number+4
    if distance==1 or 0:
        print("��Ӯ��")
    elif distance==2 or 3:
        print("�����Ӯ��")
    else:
        print("ƽ��")


    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����c����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�










    #����������ʾ��дִ�д��룬������ɺ�ɾ����pass




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

