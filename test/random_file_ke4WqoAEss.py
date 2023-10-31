所在位置 行:1 字符: 69
+ ... m -InputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -jo ...
+                                                               ~~~
表达式或语句中包含意外的标记“256”。
所在位置 行:1 字符: 67
+ ... Random -InputObject (1..1000000) | ForEach-Object { [char]($_  256) } ...
+                                                                  ~
表达式中缺少右“)”。
所在位置 行:1 字符: 56
+ (Get-Random -InputObject (1..1000000) | ForEach-Object { [char]($_  2 ...
+                                                        ~
语句块或类型定义中缺少右“}”。
所在位置 行:1 字符: 74
+ ... InputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -join  ...
+                                                                 ~
表达式或语句中包含意外的标记“}”。
所在位置 行:1 字符: 75
+ ... nputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -join ' ...
+                                                                 ~
表达式或语句中包含意外的标记“)”。
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken
 
