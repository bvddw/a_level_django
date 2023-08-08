/* put database initialization script here */

-- for example
CREATE ROLE postsuser WITH ENCRYPTED PASSWORD 'password' LOGIN;
COMMENT ON ROLE postsuser IS 'docker user for tests';

CREATE DATABASE mypostsdb OWNER postsuser;
COMMENT ON DATABASE mypostsdb IS 'docker db for tests owned by docker user';
