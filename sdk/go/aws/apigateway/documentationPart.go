// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The “AWS::ApiGateway::DocumentationPart“ resource creates a documentation part for an API. For more information, see [Representation of API Documentation in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html) in the *API Gateway Developer Guide*.
type DocumentationPart struct {
	pulumi.CustomResourceState

	DocumentationPartId pulumi.StringOutput `pulumi:"documentationPartId"`
	// The location of the targeted API entity of the to-be-created documentation part.
	Location DocumentationPartLocationOutput `pulumi:"location"`
	// The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.
	Properties pulumi.StringOutput `pulumi:"properties"`
	// The string identifier of the associated RestApi.
	RestApiId pulumi.StringOutput `pulumi:"restApiId"`
}

// NewDocumentationPart registers a new resource with the given unique name, arguments, and options.
func NewDocumentationPart(ctx *pulumi.Context,
	name string, args *DocumentationPartArgs, opts ...pulumi.ResourceOption) (*DocumentationPart, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Location == nil {
		return nil, errors.New("invalid value for required argument 'Location'")
	}
	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	if args.RestApiId == nil {
		return nil, errors.New("invalid value for required argument 'RestApiId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"location",
		"restApiId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DocumentationPart
	err := ctx.RegisterResource("aws-native:apigateway:DocumentationPart", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDocumentationPart gets an existing DocumentationPart resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDocumentationPart(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DocumentationPartState, opts ...pulumi.ResourceOption) (*DocumentationPart, error) {
	var resource DocumentationPart
	err := ctx.ReadResource("aws-native:apigateway:DocumentationPart", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DocumentationPart resources.
type documentationPartState struct {
}

type DocumentationPartState struct {
}

func (DocumentationPartState) ElementType() reflect.Type {
	return reflect.TypeOf((*documentationPartState)(nil)).Elem()
}

type documentationPartArgs struct {
	// The location of the targeted API entity of the to-be-created documentation part.
	Location DocumentationPartLocation `pulumi:"location"`
	// The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.
	Properties string `pulumi:"properties"`
	// The string identifier of the associated RestApi.
	RestApiId string `pulumi:"restApiId"`
}

// The set of arguments for constructing a DocumentationPart resource.
type DocumentationPartArgs struct {
	// The location of the targeted API entity of the to-be-created documentation part.
	Location DocumentationPartLocationInput
	// The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.
	Properties pulumi.StringInput
	// The string identifier of the associated RestApi.
	RestApiId pulumi.StringInput
}

func (DocumentationPartArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*documentationPartArgs)(nil)).Elem()
}

type DocumentationPartInput interface {
	pulumi.Input

	ToDocumentationPartOutput() DocumentationPartOutput
	ToDocumentationPartOutputWithContext(ctx context.Context) DocumentationPartOutput
}

func (*DocumentationPart) ElementType() reflect.Type {
	return reflect.TypeOf((**DocumentationPart)(nil)).Elem()
}

func (i *DocumentationPart) ToDocumentationPartOutput() DocumentationPartOutput {
	return i.ToDocumentationPartOutputWithContext(context.Background())
}

func (i *DocumentationPart) ToDocumentationPartOutputWithContext(ctx context.Context) DocumentationPartOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DocumentationPartOutput)
}

func (i *DocumentationPart) ToOutput(ctx context.Context) pulumix.Output[*DocumentationPart] {
	return pulumix.Output[*DocumentationPart]{
		OutputState: i.ToDocumentationPartOutputWithContext(ctx).OutputState,
	}
}

type DocumentationPartOutput struct{ *pulumi.OutputState }

func (DocumentationPartOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DocumentationPart)(nil)).Elem()
}

func (o DocumentationPartOutput) ToDocumentationPartOutput() DocumentationPartOutput {
	return o
}

func (o DocumentationPartOutput) ToDocumentationPartOutputWithContext(ctx context.Context) DocumentationPartOutput {
	return o
}

func (o DocumentationPartOutput) ToOutput(ctx context.Context) pulumix.Output[*DocumentationPart] {
	return pulumix.Output[*DocumentationPart]{
		OutputState: o.OutputState,
	}
}

func (o DocumentationPartOutput) DocumentationPartId() pulumi.StringOutput {
	return o.ApplyT(func(v *DocumentationPart) pulumi.StringOutput { return v.DocumentationPartId }).(pulumi.StringOutput)
}

// The location of the targeted API entity of the to-be-created documentation part.
func (o DocumentationPartOutput) Location() DocumentationPartLocationOutput {
	return o.ApplyT(func(v *DocumentationPart) DocumentationPartLocationOutput { return v.Location }).(DocumentationPartLocationOutput)
}

// The new documentation content map of the targeted API entity. Enclosed key-value pairs are API-specific, but only OpenAPI-compliant key-value pairs can be exported and, hence, published.
func (o DocumentationPartOutput) Properties() pulumi.StringOutput {
	return o.ApplyT(func(v *DocumentationPart) pulumi.StringOutput { return v.Properties }).(pulumi.StringOutput)
}

// The string identifier of the associated RestApi.
func (o DocumentationPartOutput) RestApiId() pulumi.StringOutput {
	return o.ApplyT(func(v *DocumentationPart) pulumi.StringOutput { return v.RestApiId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DocumentationPartInput)(nil)).Elem(), &DocumentationPart{})
	pulumi.RegisterOutputType(DocumentationPartOutput{})
}
