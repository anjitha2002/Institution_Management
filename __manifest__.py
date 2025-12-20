{
    'name': "Institution Management System",
    'version': '19.0.1.0.0',
    'category': 'Students, Teacher,Course,Batch',
    'sequence':6,
    'summary':'Get details of institutions',
    'description': """
    Institution Management System
       Manages :

""",
    'depends':[],
'data':[
    'security/ir.model.access.csv',
    'views/student_views.xml',
'views/teacher_views.xml',
    'views/course_views.xml',
    'views/category_views.xml',
    'views/batch_views.xml',
    'views/attendance_views.xml',
    'views/fee_payment_views.xml',
    'views/menu.xml',


],
'installable':True,
'application':True,


}