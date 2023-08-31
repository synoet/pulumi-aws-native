// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Schema for AWS::ApiGatewayV2::ApiMapping
type ApiMapping struct {
	pulumi.CustomResourceState

	// The API identifier
	ApiId pulumi.StringOutput `pulumi:"apiId"`
	// Api Mapping Id generated by service
	ApiMappingId pulumi.StringOutput `pulumi:"apiMappingId"`
	// The API mapping key
	ApiMappingKey pulumi.StringPtrOutput `pulumi:"apiMappingKey"`
	// The domain name
	DomainName pulumi.StringOutput `pulumi:"domainName"`
	// The API stage
	Stage pulumi.StringOutput `pulumi:"stage"`
}

// NewApiMapping registers a new resource with the given unique name, arguments, and options.
func NewApiMapping(ctx *pulumi.Context,
	name string, args *ApiMappingArgs, opts ...pulumi.ResourceOption) (*ApiMapping, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiId == nil {
		return nil, errors.New("invalid value for required argument 'ApiId'")
	}
	if args.DomainName == nil {
		return nil, errors.New("invalid value for required argument 'DomainName'")
	}
	if args.Stage == nil {
		return nil, errors.New("invalid value for required argument 'Stage'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"domainName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ApiMapping
	err := ctx.RegisterResource("aws-native:apigatewayv2:ApiMapping", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApiMapping gets an existing ApiMapping resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApiMapping(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApiMappingState, opts ...pulumi.ResourceOption) (*ApiMapping, error) {
	var resource ApiMapping
	err := ctx.ReadResource("aws-native:apigatewayv2:ApiMapping", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApiMapping resources.
type apiMappingState struct {
}

type ApiMappingState struct {
}

func (ApiMappingState) ElementType() reflect.Type {
	return reflect.TypeOf((*apiMappingState)(nil)).Elem()
}

type apiMappingArgs struct {
	// The API identifier
	ApiId string `pulumi:"apiId"`
	// The API mapping key
	ApiMappingKey *string `pulumi:"apiMappingKey"`
	// The domain name
	DomainName string `pulumi:"domainName"`
	// The API stage
	Stage string `pulumi:"stage"`
}

// The set of arguments for constructing a ApiMapping resource.
type ApiMappingArgs struct {
	// The API identifier
	ApiId pulumi.StringInput
	// The API mapping key
	ApiMappingKey pulumi.StringPtrInput
	// The domain name
	DomainName pulumi.StringInput
	// The API stage
	Stage pulumi.StringInput
}

func (ApiMappingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*apiMappingArgs)(nil)).Elem()
}

type ApiMappingInput interface {
	pulumi.Input

	ToApiMappingOutput() ApiMappingOutput
	ToApiMappingOutputWithContext(ctx context.Context) ApiMappingOutput
}

func (*ApiMapping) ElementType() reflect.Type {
	return reflect.TypeOf((**ApiMapping)(nil)).Elem()
}

func (i *ApiMapping) ToApiMappingOutput() ApiMappingOutput {
	return i.ToApiMappingOutputWithContext(context.Background())
}

func (i *ApiMapping) ToApiMappingOutputWithContext(ctx context.Context) ApiMappingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApiMappingOutput)
}

type ApiMappingOutput struct{ *pulumi.OutputState }

func (ApiMappingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ApiMapping)(nil)).Elem()
}

func (o ApiMappingOutput) ToApiMappingOutput() ApiMappingOutput {
	return o
}

func (o ApiMappingOutput) ToApiMappingOutputWithContext(ctx context.Context) ApiMappingOutput {
	return o
}

// The API identifier
func (o ApiMappingOutput) ApiId() pulumi.StringOutput {
	return o.ApplyT(func(v *ApiMapping) pulumi.StringOutput { return v.ApiId }).(pulumi.StringOutput)
}

// Api Mapping Id generated by service
func (o ApiMappingOutput) ApiMappingId() pulumi.StringOutput {
	return o.ApplyT(func(v *ApiMapping) pulumi.StringOutput { return v.ApiMappingId }).(pulumi.StringOutput)
}

// The API mapping key
func (o ApiMappingOutput) ApiMappingKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ApiMapping) pulumi.StringPtrOutput { return v.ApiMappingKey }).(pulumi.StringPtrOutput)
}

// The domain name
func (o ApiMappingOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *ApiMapping) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

// The API stage
func (o ApiMappingOutput) Stage() pulumi.StringOutput {
	return o.ApplyT(func(v *ApiMapping) pulumi.StringOutput { return v.Stage }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApiMappingInput)(nil)).Elem(), &ApiMapping{})
	pulumi.RegisterOutputType(ApiMappingOutput{})
}
