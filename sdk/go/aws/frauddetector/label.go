// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package frauddetector

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html
type Label struct {
	pulumi.CustomResourceState

	Arn         pulumi.StringOutput `pulumi:"arn"`
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
	Description     pulumi.StringPtrOutput `pulumi:"description"`
	LastUpdatedTime pulumi.StringOutput    `pulumi:"lastUpdatedTime"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
	Name pulumi.StringOutput `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewLabel registers a new resource with the given unique name, arguments, and options.
func NewLabel(ctx *pulumi.Context,
	name string, args *LabelArgs, opts ...pulumi.ResourceOption) (*Label, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource Label
	err := ctx.RegisterResource("aws-native:frauddetector:Label", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLabel gets an existing Label resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLabel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LabelState, opts ...pulumi.ResourceOption) (*Label, error) {
	var resource Label
	err := ctx.ReadResource("aws-native:frauddetector:Label", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Label resources.
type labelState struct {
}

type LabelState struct {
}

func (LabelState) ElementType() reflect.Type {
	return reflect.TypeOf((*labelState)(nil)).Elem()
}

type labelArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
	Name string `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Label resource.
type LabelArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
	Name pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
	Tags aws.TagArrayInput
}

func (LabelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*labelArgs)(nil)).Elem()
}

type LabelInput interface {
	pulumi.Input

	ToLabelOutput() LabelOutput
	ToLabelOutputWithContext(ctx context.Context) LabelOutput
}

func (*Label) ElementType() reflect.Type {
	return reflect.TypeOf((*Label)(nil))
}

func (i *Label) ToLabelOutput() LabelOutput {
	return i.ToLabelOutputWithContext(context.Background())
}

func (i *Label) ToLabelOutputWithContext(ctx context.Context) LabelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LabelOutput)
}

type LabelOutput struct{ *pulumi.OutputState }

func (LabelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Label)(nil))
}

func (o LabelOutput) ToLabelOutput() LabelOutput {
	return o
}

func (o LabelOutput) ToLabelOutputWithContext(ctx context.Context) LabelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LabelOutput{})
}
