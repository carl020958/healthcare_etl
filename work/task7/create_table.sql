
create table person (
	 person_id bigint not null
	,year_of_birth integer not null
	,month_of_birth integer
	,day_of_birth integer
	,death_date date
	,gender_value varchar(50)
	,race_value varchar(50)
	,ethnicity_value varchar(50)
	,primary key (person_id)
);


create table visit_occurence (
	 visit_occurrence_id bigint not null
	,person_id bigint not null
	,visit_start_date date
	,care_site_nm text
	,visit_type_value varchar(50)
	,primary key (visit_occurrence_id)
	,foreign key (person_id) references person (person_id)
);

-- clinical_note의 경우 drug_exposure이 없는 경우가 존재해, not null 제한 품
create table drug_exposure (
	 drug_exposure_id bigint not null
	,person_id bigint not null
	,drug_exposure_start_date date
	,drug_value text
	,route_value varchar(50)
	,dose_value varchar(50)
	,unit_value varchar(50)
	,visit_occurrence_id bigint 
	,primary key (drug_exposure_id)
	,foreign key (person_id) references person (person_id)
	,foreign key (visit_occurrence_id) references visit_occurence (visit_occurrence_id)	
);


create table condition_occurrence (
	 condition_occurrence_id bigint not null
	,person_id bigint not null
	,condition_start_date date not null
	,condition_value text
	,visit_occurrence_id bigint 
	,primary key (condition_occurrence_id)
	,foreign key (person_id) references person (person_id)
	,foreign key (visit_occurrence_id) references visit_occurence (visit_occurrence_id)	
);