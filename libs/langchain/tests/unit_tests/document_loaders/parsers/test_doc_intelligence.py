"""Tests for the Google Cloud DocAI parser."""
from unittest.mock import patch

import pytest

from langchain.document_loaders.parsers import DocumentIntelligenceParser


@pytest.mark.requires("azure.ai", "azure.ai.documentintelligence")
@patch("azure.ai.documentintelligence.DocumentIntelligenceClient")
@patch("azure.core.credentials.AzureKeyCredential")
def test_docai_parser_valid_processor_name(mock_credential, mock_client) -> None:
    endpoint = "endpoint"
    key = "key"

    parser = DocumentIntelligenceParser(api_endpoint=endpoint, api_key=key)
    mock_credential.assert_called_once_with(key)
    mock_client.assert_called_once_with(endpoint=endpoint, credential=mock_credential())
    assert parser.client == mock_client()
    assert parser.api_model == "prebuilt-document"
    assert parser.mode == "markdown"