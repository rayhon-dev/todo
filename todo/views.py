from django.http import HttpResponse

def todo_list(request):
    html_reponse = """
        <style>


        h1 {
            text-align: center;
            color: blue;
            background-color: beige;
        }


        form {
            width: 15%;
            margin: 0 auto;
            padding: 40px;
        }


        label {
            font-weight: bold; 
        }


        button {
            padding: 10px 20px;
            background-color: blue;
            color: white;
            border: none;

        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .highlight {
            background-color: #e9f7ff;
        }
        
        </style>


        <h1>Yangi vazifa yaratish</h1>


        <form>
            <label>Vazifa nomi:</label>
            <input type="text">

            <br> <br>

            <label>Tavsif:</label>
            <textarea>

            </textarea>

            <br> <br>

            <label>Muddati:</label>
            <input type="date">

            <br> <br>

            <label>Muhimlik darajasi:</label>

                <select>
                    <option>Past</option>
                    <option>O'rta</option>
                    <option>Yuqori</option>
                </select>

            <br> <br>   

            <button type="submit">Vazifani saqlash</button>

        </form>
        
        <table class="table table-border table-dark">
        
            <thead>
                <tr>
                    <th>Vazifa</th>
                    <th>Tavsif</th>
                    <th>Muhimlilik</th>
                    <th>Muddat</th>
                    <th>Holat</th>
                    
                </tr>
            </thead>
            <thbody>
                 <tr>
                     <td>Hisobot tayyorlash</td>
                     <td>Oylik moliyaviy hisobotni tayyorlash va topshirish</td>
                     <td>Yuqori</td>
                     <td>2023-05-31</td>
                     <td>Bajarilmoqda</td>
                </tr>
                
                <tr>
                    <td>Mijoz bilan uchrashuv</td>
                    <td>Yangi loyiha bo'yicha mijoz bilan muzokaralar o'tkazish</td>
                    <td>O'rta</td> 
                    <td>2023-05-25</td> 
                    <td>Rejalashtirilgan</td> 
                </tr>
                
                <tr>
                    <td>Prezentatsiya tayyorlash</td>
                    <td>Yangi mahsulot uchun taqdimot slaydlarini tayyorlash</td>
                    <td>Past</td> 
                    <td>2023-06-05</td> 
                    <td>Boshlanmagan</td> 
                </tr>
                
                <tr>
                    <td>Xodimlar uchun trening</td>
                    <td>Yangi dasturiy ta'minot bo'yicha xodimlarga qo'llanma berish</td>
                    <td>O'rta</td> 
                    <td>2023-06-10</td> 
                    <td>Rejalashtirilgan</td> 
                </tr>
                
                <tr>
                    <td>Xodimlar uchun trening</td>
                    <td>Yangi dasturiy ta'minot bo'yicha xodimlarga qo'llanma berish</td>
                    <td>O'rta</td> 
                    <td>2023-06-10</td> 
                    <td>Rejalashtirilgan</td> 
                </tr>
                
                <tr>
                    <td>Loyiha hujjatlarini yangilash</td>
                    <td>Joriy loyihaning tenik hujjatlarini yangilash va arxivlash</td>
                    <td>Past</td> 
                    <td>2023-06-15</td> 
                    <td>Boshlanmagan</td> 
                </tr>
            </thbody>
            
        </table>    
        
    """
    return HttpResponse(html_reponse)

