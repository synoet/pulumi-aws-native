// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html
type Crawler struct {
	pulumi.CustomResourceState

	// The attributes associated with the resource
	Attributes CrawlerAttributesOutput `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrOutput `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata pulumi.AnyOutput `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties CrawlerPropertiesOutput `pulumi:"properties"`
}

// NewCrawler registers a new resource with the given unique name, arguments, and options.
func NewCrawler(ctx *pulumi.Context,
	name string, args *CrawlerArgs, opts ...pulumi.ResourceOption) (*Crawler, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Properties == nil {
		return nil, errors.New("invalid value for required argument 'Properties'")
	}
	var resource Crawler
	err := ctx.RegisterResource("cloudformation:Glue:Crawler", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCrawler gets an existing Crawler resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCrawler(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CrawlerState, opts ...pulumi.ResourceOption) (*Crawler, error) {
	var resource Crawler
	err := ctx.ReadResource("cloudformation:Glue:Crawler", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Crawler resources.
type crawlerState struct {
	// The attributes associated with the resource
	Attributes *CrawlerAttributes `pulumi:"attributes"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties *CrawlerProperties `pulumi:"properties"`
}

type CrawlerState struct {
	// The attributes associated with the resource
	Attributes CrawlerAttributesPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties CrawlerPropertiesPtrInput
}

func (CrawlerState) ElementType() reflect.Type {
	return reflect.TypeOf((*crawlerState)(nil)).Elem()
}

type crawlerArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy *string `pulumi:"deletionPolicy"`
	// An explicit logical ID for the resource
	LogicalId *string `pulumi:"logicalId"`
	// Arbitrary structured data associated with the resource
	Metadata interface{} `pulumi:"metadata"`
	// The input properties associated with the resource
	Properties CrawlerProperties `pulumi:"properties"`
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy *string `pulumi:"updateReplacePolicy"`
}

// The set of arguments for constructing a Crawler resource.
type CrawlerArgs struct {
	// With the deletionPolicy attribute you can preserve or (in some cases) backup a resource when its stack is deleted. You can specify a deletionPolicy attribute for each resource that you want to control. If a resource has no deletionPolicy attribute, AWS CloudFormation deletes the resource by default.
	DeletionPolicy pulumi.StringPtrInput
	// An explicit logical ID for the resource
	LogicalId pulumi.StringPtrInput
	// Arbitrary structured data associated with the resource
	Metadata pulumi.Input
	// The input properties associated with the resource
	Properties CrawlerPropertiesInput
	// Use the updateReplacePolicy attribute to retain or (in some cases) backup the existing physical instance of a resource when it is replaced during a stack update operation.
	UpdateReplacePolicy pulumi.StringPtrInput
}

func (CrawlerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*crawlerArgs)(nil)).Elem()
}

type CrawlerInput interface {
	pulumi.Input

	ToCrawlerOutput() CrawlerOutput
	ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput
}

func (*Crawler) ElementType() reflect.Type {
	return reflect.TypeOf((*Crawler)(nil))
}

func (i *Crawler) ToCrawlerOutput() CrawlerOutput {
	return i.ToCrawlerOutputWithContext(context.Background())
}

func (i *Crawler) ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrawlerOutput)
}

type CrawlerOutput struct {
	*pulumi.OutputState
}

func (CrawlerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Crawler)(nil))
}

func (o CrawlerOutput) ToCrawlerOutput() CrawlerOutput {
	return o
}

func (o CrawlerOutput) ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(CrawlerOutput{})
}