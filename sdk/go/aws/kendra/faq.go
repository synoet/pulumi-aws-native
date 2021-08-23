// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kendra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html
type Faq struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
	FileFormat pulumi.StringPtrOutput `pulumi:"fileFormat"`
	Id         pulumi.StringOutput    `pulumi:"id"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
	IndexId pulumi.StringOutput `pulumi:"indexId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
	Name pulumi.StringOutput `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
	S3Path FaqS3PathOutput `pulumi:"s3Path"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewFaq registers a new resource with the given unique name, arguments, and options.
func NewFaq(ctx *pulumi.Context,
	name string, args *FaqArgs, opts ...pulumi.ResourceOption) (*Faq, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.IndexId == nil {
		return nil, errors.New("invalid value for required argument 'IndexId'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	if args.S3Path == nil {
		return nil, errors.New("invalid value for required argument 'S3Path'")
	}
	var resource Faq
	err := ctx.RegisterResource("aws-native:kendra:Faq", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFaq gets an existing Faq resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFaq(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FaqState, opts ...pulumi.ResourceOption) (*Faq, error) {
	var resource Faq
	err := ctx.ReadResource("aws-native:kendra:Faq", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Faq resources.
type faqState struct {
}

type FaqState struct {
}

func (FaqState) ElementType() reflect.Type {
	return reflect.TypeOf((*faqState)(nil)).Elem()
}

type faqArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
	Description *string `pulumi:"description"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
	FileFormat *string `pulumi:"fileFormat"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
	IndexId string `pulumi:"indexId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
	Name string `pulumi:"name"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
	RoleArn string `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
	S3Path FaqS3Path `pulumi:"s3Path"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Faq resource.
type FaqArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-description
	Description pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-fileformat
	FileFormat pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-indexid
	IndexId pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-name
	Name pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-rolearn
	RoleArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-s3path
	S3Path FaqS3PathInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-faq.html#cfn-kendra-faq-tags
	Tags aws.TagArrayInput
}

func (FaqArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*faqArgs)(nil)).Elem()
}

type FaqInput interface {
	pulumi.Input

	ToFaqOutput() FaqOutput
	ToFaqOutputWithContext(ctx context.Context) FaqOutput
}

func (*Faq) ElementType() reflect.Type {
	return reflect.TypeOf((*Faq)(nil))
}

func (i *Faq) ToFaqOutput() FaqOutput {
	return i.ToFaqOutputWithContext(context.Background())
}

func (i *Faq) ToFaqOutputWithContext(ctx context.Context) FaqOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FaqOutput)
}

type FaqOutput struct{ *pulumi.OutputState }

func (FaqOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Faq)(nil))
}

func (o FaqOutput) ToFaqOutput() FaqOutput {
	return o
}

func (o FaqOutput) ToFaqOutputWithContext(ctx context.Context) FaqOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FaqOutput{})
}
