BEGIN;
-- Create model Category
CREATE TABLE "quiz_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "description" text NOT NULL, "created_at" datetime NOT NULL);
-- Create model Quiz
CREATE TABLE "quiz_quiz" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "description" text NOT NULL, "created_at" datetime NOT NULL, "is_active" bool NOT NULL, "time_limit" integer unsigned NOT NULL CHECK ("time_limit" >= 0), "category_id" bigint NOT NULL REFERENCES "quiz_category" ("id") DEFERRABLE INITIALLY DEFERRED);
-- Create model Question
CREATE TABLE "quiz_question" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" varchar(500) NOT NULL, "difficulty" varchar(20) NOT NULL, "points" integer unsigned NOT NULL CHECK ("points" >= 0), "created_at" datetime NOT NULL, "quiz_id" bigint NOT NULL REFERENCES "quiz_quiz" ("id") DEFERRABLE INITIALLY DEFERRED);
-- Create model QuizAttempt
CREATE TABLE "quiz_quizattempt" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "score" integer NOT NULL, "max_score" integer NOT NULL, "percentage" real NOT NULL, "completed_at" datetime NOT NULL, "time_taken" integer unsigned NOT NULL CHECK ("time_taken" >= 0), "quiz_id" bigint NOT NULL REFERENCES "quiz_quiz" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
-- Create model Option
CREATE TABLE "quiz_option" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" varchar(255) NOT NULL, "is_correct" bool NOT NULL, "question_id" bigint NOT NULL REFERENCES "quiz_question" ("id") DEFERRABLE INITIALLY DEFERRED);
-- Create indexes
CREATE INDEX "quiz_quiz_categor_8a6e05_idx" ON "quiz_quiz" ("category_id");
CREATE INDEX "quiz_quiz_is_acti_71e796_idx" ON "quiz_quiz" ("is_active");
CREATE INDEX "quiz_quiz_created_aa0813_idx" ON "quiz_quiz" ("created_at" DESC);
CREATE INDEX "quiz_questi_quiz_id_57d9fe_idx" ON "quiz_question" ("quiz_id");
CREATE INDEX "quiz_questi_difficu_fde0f8_idx" ON "quiz_question" ("difficulty");
CREATE INDEX "quiz_quizat_user_id_67c058_idx" ON "quiz_quizattempt" ("user_id");
CREATE INDEX "quiz_quizat_quiz_id_ceb427_idx" ON "quiz_quizattempt" ("quiz_id");
CREATE INDEX "quiz_quizat_complet_377ef1_idx" ON "quiz_quizattempt" ("completed_at" DESC);
CREATE INDEX "quiz_quizat_percent_808d2a_idx" ON "quiz_quizattempt" ("percentage");
CREATE INDEX "quiz_catego_name_f05e58_idx" ON "quiz_category" ("name");
CREATE INDEX "quiz_quiz_category_id_568a4c23" ON "quiz_quiz" ("category_id");
CREATE INDEX "quiz_question_quiz_id_b7429966" ON "quiz_question" ("quiz_id");
CREATE INDEX "quiz_quizattempt_quiz_id_2c7782a0" ON "quiz_quizattempt" ("quiz_id");
CREATE INDEX "quiz_quizattempt_user_id_380ce10d" ON "quiz_quizattempt" ("user_id");
CREATE INDEX "quiz_option_question_id_f88cc373" ON "quiz_option" ("question_id");
CREATE INDEX "quiz_option_questio_65d165_idx" ON "quiz_option" ("question_id");
COMMIT;