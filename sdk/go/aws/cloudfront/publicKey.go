// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudfront

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudFront::PublicKey
type PublicKey struct {
	pulumi.CustomResourceState

	CreatedTime     pulumi.StringOutput   `pulumi:"createdTime"`
	PublicKeyConfig PublicKeyConfigOutput `pulumi:"publicKeyConfig"`
}

// NewPublicKey registers a new resource with the given unique name, arguments, and options.
func NewPublicKey(ctx *pulumi.Context,
	name string, args *PublicKeyArgs, opts ...pulumi.ResourceOption) (*PublicKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PublicKeyConfig == nil {
		return nil, errors.New("invalid value for required argument 'PublicKeyConfig'")
	}
	var resource PublicKey
	err := ctx.RegisterResource("aws-native:cloudfront:PublicKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPublicKey gets an existing PublicKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPublicKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PublicKeyState, opts ...pulumi.ResourceOption) (*PublicKey, error) {
	var resource PublicKey
	err := ctx.ReadResource("aws-native:cloudfront:PublicKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PublicKey resources.
type publicKeyState struct {
}

type PublicKeyState struct {
}

func (PublicKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*publicKeyState)(nil)).Elem()
}

type publicKeyArgs struct {
	PublicKeyConfig PublicKeyConfig `pulumi:"publicKeyConfig"`
}

// The set of arguments for constructing a PublicKey resource.
type PublicKeyArgs struct {
	PublicKeyConfig PublicKeyConfigInput
}

func (PublicKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*publicKeyArgs)(nil)).Elem()
}

type PublicKeyInput interface {
	pulumi.Input

	ToPublicKeyOutput() PublicKeyOutput
	ToPublicKeyOutputWithContext(ctx context.Context) PublicKeyOutput
}

func (*PublicKey) ElementType() reflect.Type {
	return reflect.TypeOf((*PublicKey)(nil))
}

func (i *PublicKey) ToPublicKeyOutput() PublicKeyOutput {
	return i.ToPublicKeyOutputWithContext(context.Background())
}

func (i *PublicKey) ToPublicKeyOutputWithContext(ctx context.Context) PublicKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PublicKeyOutput)
}

type PublicKeyOutput struct{ *pulumi.OutputState }

func (PublicKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PublicKey)(nil))
}

func (o PublicKeyOutput) ToPublicKeyOutput() PublicKeyOutput {
	return o
}

func (o PublicKeyOutput) ToPublicKeyOutputWithContext(ctx context.Context) PublicKeyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(PublicKeyOutput{})
}
