# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetFormResult',
    'AwaitableGetFormResult',
    'get_form',
    'get_form_output',
]

@pulumi.output_type
class GetFormResult:
    def __init__(__self__, app_id=None, cta=None, data_type=None, environment_name=None, fields=None, form_action_type=None, id=None, label_decorator=None, name=None, schema_version=None, sectional_elements=None, style=None):
        if app_id and not isinstance(app_id, str):
            raise TypeError("Expected argument 'app_id' to be a str")
        pulumi.set(__self__, "app_id", app_id)
        if cta and not isinstance(cta, dict):
            raise TypeError("Expected argument 'cta' to be a dict")
        pulumi.set(__self__, "cta", cta)
        if data_type and not isinstance(data_type, dict):
            raise TypeError("Expected argument 'data_type' to be a dict")
        pulumi.set(__self__, "data_type", data_type)
        if environment_name and not isinstance(environment_name, str):
            raise TypeError("Expected argument 'environment_name' to be a str")
        pulumi.set(__self__, "environment_name", environment_name)
        if fields and not isinstance(fields, dict):
            raise TypeError("Expected argument 'fields' to be a dict")
        pulumi.set(__self__, "fields", fields)
        if form_action_type and not isinstance(form_action_type, str):
            raise TypeError("Expected argument 'form_action_type' to be a str")
        pulumi.set(__self__, "form_action_type", form_action_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label_decorator and not isinstance(label_decorator, str):
            raise TypeError("Expected argument 'label_decorator' to be a str")
        pulumi.set(__self__, "label_decorator", label_decorator)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schema_version and not isinstance(schema_version, str):
            raise TypeError("Expected argument 'schema_version' to be a str")
        pulumi.set(__self__, "schema_version", schema_version)
        if sectional_elements and not isinstance(sectional_elements, dict):
            raise TypeError("Expected argument 'sectional_elements' to be a dict")
        pulumi.set(__self__, "sectional_elements", sectional_elements)
        if style and not isinstance(style, dict):
            raise TypeError("Expected argument 'style' to be a dict")
        pulumi.set(__self__, "style", style)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def cta(self) -> Optional['outputs.FormCta']:
        return pulumi.get(self, "cta")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> Optional['outputs.FormDataTypeConfig']:
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[str]:
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter
    def fields(self) -> Optional['outputs.FormFieldsMap']:
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter(name="formActionType")
    def form_action_type(self) -> Optional['FormActionType']:
        return pulumi.get(self, "form_action_type")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labelDecorator")
    def label_decorator(self) -> Optional['FormLabelDecorator']:
        return pulumi.get(self, "label_decorator")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaVersion")
    def schema_version(self) -> Optional[str]:
        return pulumi.get(self, "schema_version")

    @property
    @pulumi.getter(name="sectionalElements")
    def sectional_elements(self) -> Optional['outputs.FormSectionalElementMap']:
        return pulumi.get(self, "sectional_elements")

    @property
    @pulumi.getter
    def style(self) -> Optional['outputs.FormStyle']:
        return pulumi.get(self, "style")


class AwaitableGetFormResult(GetFormResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFormResult(
            app_id=self.app_id,
            cta=self.cta,
            data_type=self.data_type,
            environment_name=self.environment_name,
            fields=self.fields,
            form_action_type=self.form_action_type,
            id=self.id,
            label_decorator=self.label_decorator,
            name=self.name,
            schema_version=self.schema_version,
            sectional_elements=self.sectional_elements,
            style=self.style)


def get_form(app_id: Optional[str] = None,
             environment_name: Optional[str] = None,
             id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFormResult:
    """
    Definition of AWS::AmplifyUIBuilder::Form Resource Type
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['environmentName'] = environment_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:amplifyuibuilder:getForm', __args__, opts=opts, typ=GetFormResult).value

    return AwaitableGetFormResult(
        app_id=pulumi.get(__ret__, 'app_id'),
        cta=pulumi.get(__ret__, 'cta'),
        data_type=pulumi.get(__ret__, 'data_type'),
        environment_name=pulumi.get(__ret__, 'environment_name'),
        fields=pulumi.get(__ret__, 'fields'),
        form_action_type=pulumi.get(__ret__, 'form_action_type'),
        id=pulumi.get(__ret__, 'id'),
        label_decorator=pulumi.get(__ret__, 'label_decorator'),
        name=pulumi.get(__ret__, 'name'),
        schema_version=pulumi.get(__ret__, 'schema_version'),
        sectional_elements=pulumi.get(__ret__, 'sectional_elements'),
        style=pulumi.get(__ret__, 'style'))


@_utilities.lift_output_func(get_form)
def get_form_output(app_id: Optional[pulumi.Input[str]] = None,
                    environment_name: Optional[pulumi.Input[str]] = None,
                    id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFormResult]:
    """
    Definition of AWS::AmplifyUIBuilder::Form Resource Type
    """
    ...
