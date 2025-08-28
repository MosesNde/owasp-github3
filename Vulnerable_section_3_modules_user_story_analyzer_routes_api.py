 from flask import Blueprint, jsonify, request
from config.configuration import API_PREFIX, JIRA_LINK, DUMMY_ANALYSIS
 from services.gemini_sdk import get_gemini_response
 from helpers.general_helpers import replace_placeholders, get_dynamic_values
 from services.atlassian_sdk import get_jira_issue, create_jira_issue