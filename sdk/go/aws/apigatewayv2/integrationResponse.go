// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The “AWS::ApiGatewayV2::IntegrationResponse“ resource updates an integration response for an WebSocket API. For more information, see [Set up WebSocket API Integration Responses in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html) in the *API Gateway Developer Guide*.
type IntegrationResponse struct {
	pulumi.CustomResourceState

	// The API identifier.
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT``, with the following behaviors:
	//   ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
	//   ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.
	//  If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
	ContentHandlingStrategy pulumi.StringPtrOutput `pulumi:"contentHandlingStrategy"`
	// The integration ID.
	IntegrationId         pulumi.StringOutput `pulumi:"integrationId"`
	IntegrationResponseId pulumi.StringOutput `pulumi:"integrationResponseId"`
	// The integration response key.
	IntegrationResponseKey pulumi.StringOutput `pulumi:"integrationResponseKey"`
	// A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}``, where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}``, where ``{name}`` is a valid and unique response header name and ``{JSON-expression}`` is a valid JSON expression without the ``$`` prefix.
	ResponseParameters pulumi.AnyOutput `pulumi:"responseParameters"`
	// The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
	ResponseTemplates pulumi.AnyOutput `pulumi:"responseTemplates"`
	// The template selection expression for the integration response. Supported only for WebSocket APIs.
	TemplateSelectionExpression pulumi.StringPtrOutput `pulumi:"templateSelectionExpression"`
}

// NewIntegrationResponse registers a new resource with the given unique name, arguments, and options.
func NewIntegrationResponse(ctx *pulumi.Context,
	name string, args *IntegrationResponseArgs, opts ...pulumi.ResourceOption) (*IntegrationResponse, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiId == nil {
		return nil, errors.New("invalid value for required argument 'ApiId'")
	}
	if args.IntegrationId == nil {
		return nil, errors.New("invalid value for required argument 'IntegrationId'")
	}
	if args.IntegrationResponseKey == nil {
		return nil, errors.New("invalid value for required argument 'IntegrationResponseKey'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"apiId",
		"integrationId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IntegrationResponse
	err := ctx.RegisterResource("aws-native:apigatewayv2:IntegrationResponse", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIntegrationResponse gets an existing IntegrationResponse resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIntegrationResponse(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IntegrationResponseState, opts ...pulumi.ResourceOption) (*IntegrationResponse, error) {
	var resource IntegrationResponse
	err := ctx.ReadResource("aws-native:apigatewayv2:IntegrationResponse", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IntegrationResponse resources.
type integrationResponseState struct {
}

type IntegrationResponseState struct {
}

func (IntegrationResponseState) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationResponseState)(nil)).Elem()
}

type integrationResponseArgs struct {
	// The API identifier.
	ApiId string `pulumi:"apiId"`
	// Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT``, with the following behaviors:
	//   ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
	//   ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.
	//  If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
	ContentHandlingStrategy *string `pulumi:"contentHandlingStrategy"`
	// The integration ID.
	IntegrationId string `pulumi:"integrationId"`
	// The integration response key.
	IntegrationResponseKey string `pulumi:"integrationResponseKey"`
	// A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}``, where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}``, where ``{name}`` is a valid and unique response header name and ``{JSON-expression}`` is a valid JSON expression without the ``$`` prefix.
	ResponseParameters interface{} `pulumi:"responseParameters"`
	// The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
	ResponseTemplates interface{} `pulumi:"responseTemplates"`
	// The template selection expression for the integration response. Supported only for WebSocket APIs.
	TemplateSelectionExpression *string `pulumi:"templateSelectionExpression"`
}

// The set of arguments for constructing a IntegrationResponse resource.
type IntegrationResponseArgs struct {
	// The API identifier.
	ApiId pulumi.StringInput
	// Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT``, with the following behaviors:
	//   ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
	//   ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.
	//  If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
	ContentHandlingStrategy pulumi.StringPtrInput
	// The integration ID.
	IntegrationId pulumi.StringInput
	// The integration response key.
	IntegrationResponseKey pulumi.StringInput
	// A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header.{name}``, where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header.{name}`` or ``integration.response.body.{JSON-expression}``, where ``{name}`` is a valid and unique response header name and ``{JSON-expression}`` is a valid JSON expression without the ``$`` prefix.
	ResponseParameters pulumi.Input
	// The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
	ResponseTemplates pulumi.Input
	// The template selection expression for the integration response. Supported only for WebSocket APIs.
	TemplateSelectionExpression pulumi.StringPtrInput
}

func (IntegrationResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*integrationResponseArgs)(nil)).Elem()
}

type IntegrationResponseInput interface {
	pulumi.Input

	ToIntegrationResponseOutput() IntegrationResponseOutput
	ToIntegrationResponseOutputWithContext(ctx context.Context) IntegrationResponseOutput
}

func (*IntegrationResponse) ElementType() reflect.Type {
	return reflect.TypeOf((**IntegrationResponse)(nil)).Elem()
}

func (i *IntegrationResponse) ToIntegrationResponseOutput() IntegrationResponseOutput {
	return i.ToIntegrationResponseOutputWithContext(context.Background())
}

func (i *IntegrationResponse) ToIntegrationResponseOutputWithContext(ctx context.Context) IntegrationResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IntegrationResponseOutput)
}

func (i *IntegrationResponse) ToOutput(ctx context.Context) pulumix.Output[*IntegrationResponse] {
	return pulumix.Output[*IntegrationResponse]{
		OutputState: i.ToIntegrationResponseOutputWithContext(ctx).OutputState,
	}
}

type IntegrationResponseOutput struct{ *pulumi.OutputState }

func (IntegrationResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IntegrationResponse)(nil)).Elem()
}

func (o IntegrationResponseOutput) ToIntegrationResponseOutput() IntegrationResponseOutput {
	return o
}

func (o IntegrationResponseOutput) ToIntegrationResponseOutputWithContext(ctx context.Context) IntegrationResponseOutput {
	return o
}

func (o IntegrationResponseOutput) ToOutput(ctx context.Context) pulumix.Output[*IntegrationResponse] {
	return pulumix.Output[*IntegrationResponse]{
		OutputState: o.OutputState,
	}
}

// The API identifier.
func (o IntegrationResponseOutput) ApiId() pulumi.StringOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringOutput { return v.ApiId }).(pulumi.StringOutput)
}

// Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are “CONVERT_TO_BINARY“ and “CONVERT_TO_TEXT“, with the following behaviors:
//
//	 ``CONVERT_TO_BINARY``: Converts a response payload from a Base64-encoded string to the corresponding binary blob.
//	 ``CONVERT_TO_TEXT``: Converts a response payload from a binary blob to a Base64-encoded string.
//	If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
func (o IntegrationResponseOutput) ContentHandlingStrategy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringPtrOutput { return v.ContentHandlingStrategy }).(pulumi.StringPtrOutput)
}

// The integration ID.
func (o IntegrationResponseOutput) IntegrationId() pulumi.StringOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringOutput { return v.IntegrationId }).(pulumi.StringOutput)
}

func (o IntegrationResponseOutput) IntegrationResponseId() pulumi.StringOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringOutput { return v.IntegrationResponseId }).(pulumi.StringOutput)
}

// The integration response key.
func (o IntegrationResponseOutput) IntegrationResponseKey() pulumi.StringOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringOutput { return v.IntegrationResponseKey }).(pulumi.StringOutput)
}

// A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of “method.response.header.{name}“, where name is a valid and unique header name. The mapped non-static value must match the pattern of “integration.response.header.{name}“ or “integration.response.body.{JSON-expression}“, where “{name}“ is a valid and unique response header name and “{JSON-expression}“ is a valid JSON expression without the “$“ prefix.
func (o IntegrationResponseOutput) ResponseParameters() pulumi.AnyOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.AnyOutput { return v.ResponseParameters }).(pulumi.AnyOutput)
}

// The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
func (o IntegrationResponseOutput) ResponseTemplates() pulumi.AnyOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.AnyOutput { return v.ResponseTemplates }).(pulumi.AnyOutput)
}

// The template selection expression for the integration response. Supported only for WebSocket APIs.
func (o IntegrationResponseOutput) TemplateSelectionExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IntegrationResponse) pulumi.StringPtrOutput { return v.TemplateSelectionExpression }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IntegrationResponseInput)(nil)).Elem(), &IntegrationResponse{})
	pulumi.RegisterOutputType(IntegrationResponseOutput{})
}
