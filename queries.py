query_detail = {1:"top 3 taskers with the most accomplished tasks ",
              2:"SELECT * FROM Tasker ",
              3:"SELECT * FROM Tasker ",
              4:"SELECT * FROM Tasker ",
              5:"SELECT * FROM Tasker ",
              6:"SELECT * FROM Tasker ",
              7:"SELECT * FROM Tasker ",
              8:"SELECT * FROM Tasker ",
              9:"SELECT * FROM Tasker ",
              10:"SELECT * FROM Tasker ",
              11:"SELECT * FROM Tasker ",
              12:"SELECT * FROM Tasker ",
              13:"SELECT * FROM Tasker ",
              14:"SELECT * FROM Tasker ",
              15:"SELECT * FROM Tasker ",
              16:"SELECT * FROM Tasker ",
              17:" ",
              18:" ",
              19:" ",
              20:""
              }

query_dict = {1:"""SELECT name, COUNT (tasker_accomplishments.accomplished_ID) AS accomplished_tasks  

FROM tasker, tasker_accomplishments 

WHERE tasker.tasker_id = tasker_accomplishments.tasker_ID 

GROUP BY name 

ORDER BY accomplished_tasks DESC 

LIMIT 3; """,
              2:"SELECT * FROM Tasker ",
              3:"SELECT * FROM Tasker ",
              4:"SELECT * FROM Tasker ",
              5:"SELECT * FROM Tasker ",
              6:"SELECT * FROM Tasker ",
              7:"SELECT * FROM Tasker ",
              8:"SELECT * FROM Tasker ",
              9:"SELECT * FROM Tasker ",
              10:"SELECT * FROM Tasker ",
              11:"SELECT * FROM Tasker ",
              12:"SELECT * FROM Tasker ",
              13:"SELECT * FROM Tasker ",
              14:"SELECT * FROM Tasker ",
              15:"SELECT * FROM Tasker ",
              16:"SELECT * FROM Tasker ",
              17:"SELECT * FROM Tasker ",
              18:"SELECT * FROM Tasker ",
              19:"SELECT * FROM Tasker ",
              20:"SELECT * FROM Tasker "
              }