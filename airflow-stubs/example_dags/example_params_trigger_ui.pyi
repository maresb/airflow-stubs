from airflow.decorators import task as task
from airflow.decorators.base import generate_english_greeting as generate_english_greeting, generate_french_greeting as generate_french_greeting, generate_german_greeting as generate_german_greeting, get_names as get_names, print_greetings as print_greetings, select_languages as select_languages
from airflow.models.dag import DAG as DAG, dag as dag
from airflow.models.param import Param as Param
from airflow.models.xcom_arg import english_greetings as english_greetings, french_greetings as french_greetings, german_greetings as german_greetings, lang_select as lang_select, names as names, results_print as results_print
from airflow.utils.trigger_rule import TriggerRule as TriggerRule

TYPE_CHECKING: bool
