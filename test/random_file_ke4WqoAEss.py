����λ�� ��:1 �ַ�: 69
+ ... m -InputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -jo ...
+                                                               ~~~
���ʽ������а�������ı�ǡ�256����
����λ�� ��:1 �ַ�: 67
+ ... Random -InputObject (1..1000000) | ForEach-Object { [char]($_  256) } ...
+                                                                  ~
���ʽ��ȱ���ҡ�)����
����λ�� ��:1 �ַ�: 56
+ (Get-Random -InputObject (1..1000000) | ForEach-Object { [char]($_  2 ...
+                                                        ~
��������Ͷ�����ȱ���ҡ�}����
����λ�� ��:1 �ַ�: 74
+ ... InputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -join  ...
+                                                                 ~
���ʽ������а�������ı�ǡ�}����
����λ�� ��:1 �ַ�: 75
+ ... nputObject (1..1000000) | ForEach-Object { [char]($_  256) }) -join ' ...
+                                                                 ~
���ʽ������а�������ı�ǡ�)����
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken
 
