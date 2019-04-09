


CREATE TABLE books (
    id integer NOT NULL,
    name character varying(80) NOT NULL,
    price double precision NOT NULL,
    isbn integer
);


ALTER TABLE books OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE books_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE books_id_seq OWNER TO postgres;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE books_id_seq OWNED BY books.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE users (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    registered_on timestamp without time zone NOT NULL,
    admin boolean NOT NULL
);


ALTER TABLE users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_id_seq OWNER TO postgres;



ALTER SEQUENCE  users_id_seq OWNED BY  users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY  books ALTER COLUMN id SET DEFAULT nextval(' books_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY  users ALTER COLUMN id SET DEFAULT nextval(' users_id_seq'::regclass);


--
-- Name: books_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY  books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: users_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY  users
    ADD CONSTRAINT users_email_key UNIQUE (email);




ALTER TABLE ONLY  users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);

