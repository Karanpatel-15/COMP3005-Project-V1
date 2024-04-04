SELECT 'DROP TABLE IF EXISTS "' || table_name || '" CASCADE;' 
FROM information_schema.tables 
WHERE table_schema = 'public';
