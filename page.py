class elem():
    # LOGIN
    username = "username"
    password = "password"
    btn_login = "orangehrm-login-button"

    # MENU
    admin = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
    job_drop = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
    job_title = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a"
    btn_add_job = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[1]/div/button"
    btn_save = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]"
    btn_cancel = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[1]"
    btn_delete = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[1]/i"
    btn_delete_up = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/div/div/button"
    btn_cancel_delete = "//*[@id='app']/div[3]/div/div/div/div[3]/button[1]"
    btn_fix_delete = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"

    # ADD JOB TITLE
    add_job_title = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input"
    add_job_desc = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea"
    add_job_spec = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[1]"
    add_note = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea"

    # EDIT JOB
    btn_edit = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[17]/div/div[4]/div/button[2]/i"

    # CHECKLIST
    check1 = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[19]/div/div[1]/div/div/label/span/i"

class link():
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    addjob_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle"
    editjob_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList"