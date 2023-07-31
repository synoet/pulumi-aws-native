// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::WAFRegional::WebACLAssociation
//
// Deprecated: WebACLAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type WebACLAssociation struct {
	pulumi.CustomResourceState

	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	WebAclId    pulumi.StringOutput `pulumi:"webAclId"`
}

// NewWebACLAssociation registers a new resource with the given unique name, arguments, and options.
func NewWebACLAssociation(ctx *pulumi.Context,
	name string, args *WebACLAssociationArgs, opts ...pulumi.ResourceOption) (*WebACLAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceArn == nil {
		return nil, errors.New("invalid value for required argument 'ResourceArn'")
	}
	if args.WebAclId == nil {
		return nil, errors.New("invalid value for required argument 'WebAclId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WebACLAssociation
	err := ctx.RegisterResource("aws-native:wafregional:WebACLAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWebACLAssociation gets an existing WebACLAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWebACLAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WebACLAssociationState, opts ...pulumi.ResourceOption) (*WebACLAssociation, error) {
	var resource WebACLAssociation
	err := ctx.ReadResource("aws-native:wafregional:WebACLAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WebACLAssociation resources.
type webACLAssociationState struct {
}

type WebACLAssociationState struct {
}

func (WebACLAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*webACLAssociationState)(nil)).Elem()
}

type webACLAssociationArgs struct {
	ResourceArn string `pulumi:"resourceArn"`
	WebAclId    string `pulumi:"webAclId"`
}

// The set of arguments for constructing a WebACLAssociation resource.
type WebACLAssociationArgs struct {
	ResourceArn pulumi.StringInput
	WebAclId    pulumi.StringInput
}

func (WebACLAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*webACLAssociationArgs)(nil)).Elem()
}

type WebACLAssociationInput interface {
	pulumi.Input

	ToWebACLAssociationOutput() WebACLAssociationOutput
	ToWebACLAssociationOutputWithContext(ctx context.Context) WebACLAssociationOutput
}

func (*WebACLAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**WebACLAssociation)(nil)).Elem()
}

func (i *WebACLAssociation) ToWebACLAssociationOutput() WebACLAssociationOutput {
	return i.ToWebACLAssociationOutputWithContext(context.Background())
}

func (i *WebACLAssociation) ToWebACLAssociationOutputWithContext(ctx context.Context) WebACLAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WebACLAssociationOutput)
}

type WebACLAssociationOutput struct{ *pulumi.OutputState }

func (WebACLAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WebACLAssociation)(nil)).Elem()
}

func (o WebACLAssociationOutput) ToWebACLAssociationOutput() WebACLAssociationOutput {
	return o
}

func (o WebACLAssociationOutput) ToWebACLAssociationOutputWithContext(ctx context.Context) WebACLAssociationOutput {
	return o
}

func (o WebACLAssociationOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *WebACLAssociation) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o WebACLAssociationOutput) WebAclId() pulumi.StringOutput {
	return o.ApplyT(func(v *WebACLAssociation) pulumi.StringOutput { return v.WebAclId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WebACLAssociationInput)(nil)).Elem(), &WebACLAssociation{})
	pulumi.RegisterOutputType(WebACLAssociationOutput{})
}
