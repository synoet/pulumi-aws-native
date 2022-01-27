// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApiGatewayV2::Api
//
// Deprecated: Api is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Api struct {
	pulumi.CustomResourceState

	ApiEndpoint               pulumi.StringOutput        `pulumi:"apiEndpoint"`
	ApiKeySelectionExpression pulumi.StringPtrOutput     `pulumi:"apiKeySelectionExpression"`
	BasePath                  pulumi.StringPtrOutput     `pulumi:"basePath"`
	Body                      pulumi.AnyOutput           `pulumi:"body"`
	BodyS3Location            ApiBodyS3LocationPtrOutput `pulumi:"bodyS3Location"`
	CorsConfiguration         ApiCorsPtrOutput           `pulumi:"corsConfiguration"`
	CredentialsArn            pulumi.StringPtrOutput     `pulumi:"credentialsArn"`
	Description               pulumi.StringPtrOutput     `pulumi:"description"`
	DisableExecuteApiEndpoint pulumi.BoolPtrOutput       `pulumi:"disableExecuteApiEndpoint"`
	DisableSchemaValidation   pulumi.BoolPtrOutput       `pulumi:"disableSchemaValidation"`
	FailOnWarnings            pulumi.BoolPtrOutput       `pulumi:"failOnWarnings"`
	Name                      pulumi.StringPtrOutput     `pulumi:"name"`
	ProtocolType              pulumi.StringPtrOutput     `pulumi:"protocolType"`
	RouteKey                  pulumi.StringPtrOutput     `pulumi:"routeKey"`
	RouteSelectionExpression  pulumi.StringPtrOutput     `pulumi:"routeSelectionExpression"`
	Tags                      pulumi.AnyOutput           `pulumi:"tags"`
	Target                    pulumi.StringPtrOutput     `pulumi:"target"`
	Version                   pulumi.StringPtrOutput     `pulumi:"version"`
}

// NewApi registers a new resource with the given unique name, arguments, and options.
func NewApi(ctx *pulumi.Context,
	name string, args *ApiArgs, opts ...pulumi.ResourceOption) (*Api, error) {
	if args == nil {
		args = &ApiArgs{}
	}

	var resource Api
	err := ctx.RegisterResource("aws-native:apigatewayv2:Api", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApi gets an existing Api resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApi(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApiState, opts ...pulumi.ResourceOption) (*Api, error) {
	var resource Api
	err := ctx.ReadResource("aws-native:apigatewayv2:Api", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Api resources.
type apiState struct {
}

type ApiState struct {
}

func (ApiState) ElementType() reflect.Type {
	return reflect.TypeOf((*apiState)(nil)).Elem()
}

type apiArgs struct {
	ApiKeySelectionExpression *string            `pulumi:"apiKeySelectionExpression"`
	BasePath                  *string            `pulumi:"basePath"`
	Body                      interface{}        `pulumi:"body"`
	BodyS3Location            *ApiBodyS3Location `pulumi:"bodyS3Location"`
	CorsConfiguration         *ApiCors           `pulumi:"corsConfiguration"`
	CredentialsArn            *string            `pulumi:"credentialsArn"`
	Description               *string            `pulumi:"description"`
	DisableExecuteApiEndpoint *bool              `pulumi:"disableExecuteApiEndpoint"`
	DisableSchemaValidation   *bool              `pulumi:"disableSchemaValidation"`
	FailOnWarnings            *bool              `pulumi:"failOnWarnings"`
	Name                      *string            `pulumi:"name"`
	ProtocolType              *string            `pulumi:"protocolType"`
	RouteKey                  *string            `pulumi:"routeKey"`
	RouteSelectionExpression  *string            `pulumi:"routeSelectionExpression"`
	Tags                      interface{}        `pulumi:"tags"`
	Target                    *string            `pulumi:"target"`
	Version                   *string            `pulumi:"version"`
}

// The set of arguments for constructing a Api resource.
type ApiArgs struct {
	ApiKeySelectionExpression pulumi.StringPtrInput
	BasePath                  pulumi.StringPtrInput
	Body                      pulumi.Input
	BodyS3Location            ApiBodyS3LocationPtrInput
	CorsConfiguration         ApiCorsPtrInput
	CredentialsArn            pulumi.StringPtrInput
	Description               pulumi.StringPtrInput
	DisableExecuteApiEndpoint pulumi.BoolPtrInput
	DisableSchemaValidation   pulumi.BoolPtrInput
	FailOnWarnings            pulumi.BoolPtrInput
	Name                      pulumi.StringPtrInput
	ProtocolType              pulumi.StringPtrInput
	RouteKey                  pulumi.StringPtrInput
	RouteSelectionExpression  pulumi.StringPtrInput
	Tags                      pulumi.Input
	Target                    pulumi.StringPtrInput
	Version                   pulumi.StringPtrInput
}

func (ApiArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*apiArgs)(nil)).Elem()
}

type ApiInput interface {
	pulumi.Input

	ToApiOutput() ApiOutput
	ToApiOutputWithContext(ctx context.Context) ApiOutput
}

func (*Api) ElementType() reflect.Type {
	return reflect.TypeOf((**Api)(nil)).Elem()
}

func (i *Api) ToApiOutput() ApiOutput {
	return i.ToApiOutputWithContext(context.Background())
}

func (i *Api) ToApiOutputWithContext(ctx context.Context) ApiOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApiOutput)
}

type ApiOutput struct{ *pulumi.OutputState }

func (ApiOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Api)(nil)).Elem()
}

func (o ApiOutput) ToApiOutput() ApiOutput {
	return o
}

func (o ApiOutput) ToApiOutputWithContext(ctx context.Context) ApiOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApiInput)(nil)).Elem(), &Api{})
	pulumi.RegisterOutputType(ApiOutput{})
}
