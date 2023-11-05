CREATE DATABASE "online_university_db" ;

CREATE USER "online_university_user" WITH PASSWORD 'Q-V3dGx8RkKKoMwwHYO06aRglj06_V_p02cE1n7fGYQ' ;

ALTER ROLE "online_university_user" SET client_encoding TO 'utf8' ;

ALTER ROLE "online_university_user" SET default_transaction_isolation TO 'read committed' ;

ALTER ROLE "online_university_user" SET timezone TO 'UTC' ;

ALTER USER "online_university_user" CREATEDB ;

GRANT ALL PRIVILEGES ON DATABASE online_university_db_2 TO "online_university_user" ;

GRANT ALL ON schema public TO "online_university_user" ;

SELECT has_schema_privilege( 'online_university_user','public','CREATE') ;

ALTER DATABASE "online_university_db_2" OWNER TO "online_university_user" ;
