// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Schema for ApiGatewayV2 Integration Response
func LookupIntegrationResponse(ctx *pulumi.Context, args *LookupIntegrationResponseArgs, opts ...pulumi.InvokeOption) (*LookupIntegrationResponseResult, error) {
	var rv LookupIntegrationResponseResult
	err := ctx.Invoke("aws-native:apigatewayv2:getIntegrationResponse", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupIntegrationResponseArgs struct {
	// The API identifier
	ApiId string `pulumi:"apiId"`
	// The integration ID
	IntegrationId string `pulumi:"integrationId"`
	// Integration Response ID generated by service
	IntegrationResponseId string `pulumi:"integrationResponseId"`
}

type LookupIntegrationResponseResult struct {
	//  Specifies how to handle response payload content type conversions
	ContentHandlingStrategy *string `pulumi:"contentHandlingStrategy"`
	// Integration Response ID generated by service
	IntegrationResponseId *string `pulumi:"integrationResponseId"`
	// The integration response key
	IntegrationResponseKey *string `pulumi:"integrationResponseKey"`
	// A key-value map specifying response parameters that are passed to the method response from the backend
	ResponseParameters interface{} `pulumi:"responseParameters"`
	// The collection of response templates for the integration response as a string-to-string map of key-value pairs
	ResponseTemplates interface{} `pulumi:"responseTemplates"`
	// The template selection expression for the integration response. Supported only for WebSocket APIs
	TemplateSelectionExpression *string `pulumi:"templateSelectionExpression"`
}

func LookupIntegrationResponseOutput(ctx *pulumi.Context, args LookupIntegrationResponseOutputArgs, opts ...pulumi.InvokeOption) LookupIntegrationResponseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIntegrationResponseResult, error) {
			args := v.(LookupIntegrationResponseArgs)
			r, err := LookupIntegrationResponse(ctx, &args, opts...)
			var s LookupIntegrationResponseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIntegrationResponseResultOutput)
}

type LookupIntegrationResponseOutputArgs struct {
	// The API identifier
	ApiId pulumi.StringInput `pulumi:"apiId"`
	// The integration ID
	IntegrationId pulumi.StringInput `pulumi:"integrationId"`
	// Integration Response ID generated by service
	IntegrationResponseId pulumi.StringInput `pulumi:"integrationResponseId"`
}

func (LookupIntegrationResponseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIntegrationResponseArgs)(nil)).Elem()
}

type LookupIntegrationResponseResultOutput struct{ *pulumi.OutputState }

func (LookupIntegrationResponseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIntegrationResponseResult)(nil)).Elem()
}

func (o LookupIntegrationResponseResultOutput) ToLookupIntegrationResponseResultOutput() LookupIntegrationResponseResultOutput {
	return o
}

func (o LookupIntegrationResponseResultOutput) ToLookupIntegrationResponseResultOutputWithContext(ctx context.Context) LookupIntegrationResponseResultOutput {
	return o
}

// Specifies how to handle response payload content type conversions
func (o LookupIntegrationResponseResultOutput) ContentHandlingStrategy() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) *string { return v.ContentHandlingStrategy }).(pulumi.StringPtrOutput)
}

// Integration Response ID generated by service
func (o LookupIntegrationResponseResultOutput) IntegrationResponseId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) *string { return v.IntegrationResponseId }).(pulumi.StringPtrOutput)
}

// The integration response key
func (o LookupIntegrationResponseResultOutput) IntegrationResponseKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) *string { return v.IntegrationResponseKey }).(pulumi.StringPtrOutput)
}

// A key-value map specifying response parameters that are passed to the method response from the backend
func (o LookupIntegrationResponseResultOutput) ResponseParameters() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) interface{} { return v.ResponseParameters }).(pulumi.AnyOutput)
}

// The collection of response templates for the integration response as a string-to-string map of key-value pairs
func (o LookupIntegrationResponseResultOutput) ResponseTemplates() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) interface{} { return v.ResponseTemplates }).(pulumi.AnyOutput)
}

// The template selection expression for the integration response. Supported only for WebSocket APIs
func (o LookupIntegrationResponseResultOutput) TemplateSelectionExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIntegrationResponseResult) *string { return v.TemplateSelectionExpression }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIntegrationResponseResultOutput{})
}
