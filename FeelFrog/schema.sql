BEGIN;
CREATE TABLE "moodEntry_activity" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(200) NOT NULL UNIQUE,
    "userCreated" bool NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "no" integer unsigned NOT NULL
)
;
CREATE TABLE "moodEntry_activities_activitys" (
    "id" integer NOT NULL PRIMARY KEY,
    "activities_id" integer NOT NULL,
    "activity_id" integer NOT NULL REFERENCES "moodEntry_activity" ("id"),
    UNIQUE ("activities_id", "activity_id")
)
;
CREATE TABLE "moodEntry_activities" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id")
)
;
CREATE TABLE "moodEntry_moodattime" (
    "id" integer NOT NULL PRIMARY KEY,
    "mood" integer unsigned NOT NULL,
    "time" datetime NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    UNIQUE ("time", "user_id")
)
;
CREATE TABLE "moodEntry_activityattime" (
    "id" integer NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "activity_id" integer NOT NULL REFERENCES "moodEntry_activity" ("id"),
    "timeStart" datetime NOT NULL,
    "timeStop" datetime NOT NULL,
    UNIQUE ("timeStart", "user_id"),
    UNIQUE ("timeStop", "user_id")
)
;
CREATE TABLE "moodEntry_activityvector" (
    "id" integer NOT NULL PRIMARY KEY,
    "vector" integer NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id")
)
;
CREATE TABLE "moodEntry_moodpredicted" (
    "id" integer NOT NULL PRIMARY KEY,
    "moodStart_id" integer NOT NULL REFERENCES "moodEntry_moodattime" ("id"),
    "moodStop_id" integer NOT NULL REFERENCES "moodEntry_moodattime" ("id"),
    "activityV_id" integer NOT NULL REFERENCES "moodEntry_activityvector" ("id"),
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    "prediction" integer NOT NULL,
    "fromTime" datetime NOT NULL,
    "toTime" datetime NOT NULL
)
;

COMMIT;
