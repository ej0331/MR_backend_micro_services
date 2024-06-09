Feature: 網頁端學生新增功能
    Scenario Outline: 新增學生
        Given teacher_account欄位為 <teacher_account>, password欄位為 <password>, student_name欄位為 <student_name>, student_account欄位為 <student_account>
        When 前往登入頁面
        And 輸入 teacher_account 和 password 後點擊登入按鈕
        And 前往 home 頁面
        And 點擊「學生帳號」側欄選項
        And 點擊「新增帳號」按鈕
        And 在「姓名」輸入框測試值
        And 在「帳號」輸入框測試值
        And 選擇「班級」下拉選單第一個選項
        And 點擊「新增」按鈕
        Then 確認學生列表有此新增的學生

        Examples:
            | teacher_account | password | student_name | student_account |
            | teacher | teacher | ejj | ejj |
            
            