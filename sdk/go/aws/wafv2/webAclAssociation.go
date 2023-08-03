// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wafv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Associates WebACL to Application Load Balancer, CloudFront or API Gateway.
type WebAclAssociation struct {
	pulumi.CustomResourceState

	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	WebAclArn   pulumi.StringOutput `pulumi:"webAclArn"`
}

// NewWebAclAssociation registers a new resource with the given unique name, arguments, and options.
func NewWebAclAssociation(ctx *pulumi.Context,
	name string, args *WebAclAssociationArgs, opts ...pulumi.ResourceOption) (*WebAclAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceArn == nil {
		return nil, errors.New("invalid value for required argument 'ResourceArn'")
	}
	if args.WebAclArn == nil {
		return nil, errors.New("invalid value for required argument 'WebAclArn'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WebAclAssociation
	err := ctx.RegisterResource("aws-native:wafv2:WebAclAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWebAclAssociation gets an existing WebAclAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebAclAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WebAclAssociationState, opts ...pulumi.ResourceOption) (*WebAclAssociation, error) {
	var resource WebAclAssociation
	err := ctx.ReadResource("aws-native:wafv2:WebAclAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WebAclAssociation resources.
type webAclAssociationState struct {
}

type WebAclAssociationState struct {
}

func (WebAclAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*webAclAssociationState)(nil)).Elem()
}

type webAclAssociationArgs struct {
	ResourceArn string `pulumi:"resourceArn"`
	WebAclArn   string `pulumi:"webAclArn"`
}

// The set of arguments for constructing a WebAclAssociation resource.
type WebAclAssociationArgs struct {
	ResourceArn pulumi.StringInput
	WebAclArn   pulumi.StringInput
}

func (WebAclAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*webAclAssociationArgs)(nil)).Elem()
}

type WebAclAssociationInput interface {
	pulumi.Input

	ToWebAclAssociationOutput() WebAclAssociationOutput
	ToWebAclAssociationOutputWithContext(ctx context.Context) WebAclAssociationOutput
}

func (*WebAclAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**WebAclAssociation)(nil)).Elem()
}

func (i *WebAclAssociation) ToWebAclAssociationOutput() WebAclAssociationOutput {
	return i.ToWebAclAssociationOutputWithContext(context.Background())
}

func (i *WebAclAssociation) ToWebAclAssociationOutputWithContext(ctx context.Context) WebAclAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebAclAssociationOutput)
}

type WebAclAssociationOutput struct{ *pulumi.OutputState }

func (WebAclAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WebAclAssociation)(nil)).Elem()
}

func (o WebAclAssociationOutput) ToWebAclAssociationOutput() WebAclAssociationOutput {
	return o
}

func (o WebAclAssociationOutput) ToWebAclAssociationOutputWithContext(ctx context.Context) WebAclAssociationOutput {
	return o
}

func (o WebAclAssociationOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *WebAclAssociation) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o WebAclAssociationOutput) WebAclArn() pulumi.StringOutput {
	return o.ApplyT(func(v *WebAclAssociation) pulumi.StringOutput { return v.WebAclArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WebAclAssociationInput)(nil)).Elem(), &WebAclAssociation{})
	pulumi.RegisterOutputType(WebAclAssociationOutput{})
}
