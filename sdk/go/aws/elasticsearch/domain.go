// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package elasticsearch

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Elasticsearch::Domain
//
// Deprecated: Domain is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Domain struct {
	pulumi.CustomResourceState

	AccessPolicies              pulumi.AnyOutput                            `pulumi:"accessPolicies"`
	AdvancedOptions             pulumi.AnyOutput                            `pulumi:"advancedOptions"`
	AdvancedSecurityOptions     DomainAdvancedSecurityOptionsInputPtrOutput `pulumi:"advancedSecurityOptions"`
	Arn                         pulumi.StringOutput                         `pulumi:"arn"`
	CognitoOptions              DomainCognitoOptionsPtrOutput               `pulumi:"cognitoOptions"`
	DomainArn                   pulumi.StringOutput                         `pulumi:"domainArn"`
	DomainEndpoint              pulumi.StringOutput                         `pulumi:"domainEndpoint"`
	DomainEndpointOptions       DomainDomainEndpointOptionsPtrOutput        `pulumi:"domainEndpointOptions"`
	DomainName                  pulumi.StringPtrOutput                      `pulumi:"domainName"`
	EBSOptions                  DomainEBSOptionsPtrOutput                   `pulumi:"eBSOptions"`
	ElasticsearchClusterConfig  DomainElasticsearchClusterConfigPtrOutput   `pulumi:"elasticsearchClusterConfig"`
	ElasticsearchVersion        pulumi.StringPtrOutput                      `pulumi:"elasticsearchVersion"`
	EncryptionAtRestOptions     DomainEncryptionAtRestOptionsPtrOutput      `pulumi:"encryptionAtRestOptions"`
	LogPublishingOptions        pulumi.AnyOutput                            `pulumi:"logPublishingOptions"`
	NodeToNodeEncryptionOptions DomainNodeToNodeEncryptionOptionsPtrOutput  `pulumi:"nodeToNodeEncryptionOptions"`
	SnapshotOptions             DomainSnapshotOptionsPtrOutput              `pulumi:"snapshotOptions"`
	Tags                        DomainTagArrayOutput                        `pulumi:"tags"`
	VPCOptions                  DomainVPCOptionsPtrOutput                   `pulumi:"vPCOptions"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		args = &DomainArgs{}
	}

	var resource Domain
	err := ctx.RegisterResource("aws-native:elasticsearch:Domain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomain gets an existing Domain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Domain, error) {
	var resource Domain
	err := ctx.ReadResource("aws-native:elasticsearch:Domain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Domain resources.
type domainState struct {
}

type DomainState struct {
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	AccessPolicies              interface{}                         `pulumi:"accessPolicies"`
	AdvancedOptions             interface{}                         `pulumi:"advancedOptions"`
	AdvancedSecurityOptions     *DomainAdvancedSecurityOptionsInput `pulumi:"advancedSecurityOptions"`
	CognitoOptions              *DomainCognitoOptions               `pulumi:"cognitoOptions"`
	DomainEndpointOptions       *DomainDomainEndpointOptions        `pulumi:"domainEndpointOptions"`
	DomainName                  *string                             `pulumi:"domainName"`
	EBSOptions                  *DomainEBSOptions                   `pulumi:"eBSOptions"`
	ElasticsearchClusterConfig  *DomainElasticsearchClusterConfig   `pulumi:"elasticsearchClusterConfig"`
	ElasticsearchVersion        *string                             `pulumi:"elasticsearchVersion"`
	EncryptionAtRestOptions     *DomainEncryptionAtRestOptions      `pulumi:"encryptionAtRestOptions"`
	LogPublishingOptions        interface{}                         `pulumi:"logPublishingOptions"`
	NodeToNodeEncryptionOptions *DomainNodeToNodeEncryptionOptions  `pulumi:"nodeToNodeEncryptionOptions"`
	SnapshotOptions             *DomainSnapshotOptions              `pulumi:"snapshotOptions"`
	Tags                        []DomainTag                         `pulumi:"tags"`
	VPCOptions                  *DomainVPCOptions                   `pulumi:"vPCOptions"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	AccessPolicies              pulumi.Input
	AdvancedOptions             pulumi.Input
	AdvancedSecurityOptions     DomainAdvancedSecurityOptionsInputPtrInput
	CognitoOptions              DomainCognitoOptionsPtrInput
	DomainEndpointOptions       DomainDomainEndpointOptionsPtrInput
	DomainName                  pulumi.StringPtrInput
	EBSOptions                  DomainEBSOptionsPtrInput
	ElasticsearchClusterConfig  DomainElasticsearchClusterConfigPtrInput
	ElasticsearchVersion        pulumi.StringPtrInput
	EncryptionAtRestOptions     DomainEncryptionAtRestOptionsPtrInput
	LogPublishingOptions        pulumi.Input
	NodeToNodeEncryptionOptions DomainNodeToNodeEncryptionOptionsPtrInput
	SnapshotOptions             DomainSnapshotOptionsPtrInput
	Tags                        DomainTagArrayInput
	VPCOptions                  DomainVPCOptionsPtrInput
}

func (DomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainArgs)(nil)).Elem()
}

type DomainInput interface {
	pulumi.Input

	ToDomainOutput() DomainOutput
	ToDomainOutputWithContext(ctx context.Context) DomainOutput
}

func (*Domain) ElementType() reflect.Type {
	return reflect.TypeOf((*Domain)(nil))
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

type DomainOutput struct{ *pulumi.OutputState }

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Domain)(nil))
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DomainOutput{})
}
