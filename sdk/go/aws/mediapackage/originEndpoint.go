// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mediapackage

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::MediaPackage::OriginEndpoint
type OriginEndpoint struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) assigned to the OriginEndpoint.
	Arn           pulumi.StringOutput                  `pulumi:"arn"`
	Authorization OriginEndpointAuthorizationPtrOutput `pulumi:"authorization"`
	// The ID of the Channel the OriginEndpoint is associated with.
	ChannelId   pulumi.StringOutput                `pulumi:"channelId"`
	CmafPackage OriginEndpointCmafPackagePtrOutput `pulumi:"cmafPackage"`
	DashPackage OriginEndpointDashPackagePtrOutput `pulumi:"dashPackage"`
	// A short text description of the OriginEndpoint.
	Description pulumi.StringPtrOutput            `pulumi:"description"`
	HlsPackage  OriginEndpointHlsPackagePtrOutput `pulumi:"hlsPackage"`
	// A short string appended to the end of the OriginEndpoint URL.
	ManifestName pulumi.StringPtrOutput            `pulumi:"manifestName"`
	MssPackage   OriginEndpointMssPackagePtrOutput `pulumi:"mssPackage"`
	// Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
	Origination OriginEndpointOriginationPtrOutput `pulumi:"origination"`
	// Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
	StartoverWindowSeconds pulumi.IntPtrOutput `pulumi:"startoverWindowSeconds"`
	// A collection of tags associated with a resource
	Tags OriginEndpointTagArrayOutput `pulumi:"tags"`
	// Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
	TimeDelaySeconds pulumi.IntPtrOutput `pulumi:"timeDelaySeconds"`
	// The URL of the packaged OriginEndpoint for consumption.
	Url pulumi.StringOutput `pulumi:"url"`
	// A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
	Whitelist pulumi.StringArrayOutput `pulumi:"whitelist"`
}

// NewOriginEndpoint registers a new resource with the given unique name, arguments, and options.
func NewOriginEndpoint(ctx *pulumi.Context,
	name string, args *OriginEndpointArgs, opts ...pulumi.ResourceOption) (*OriginEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ChannelId == nil {
		return nil, errors.New("invalid value for required argument 'ChannelId'")
	}
	var resource OriginEndpoint
	err := ctx.RegisterResource("aws-native:mediapackage:OriginEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOriginEndpoint gets an existing OriginEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOriginEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OriginEndpointState, opts ...pulumi.ResourceOption) (*OriginEndpoint, error) {
	var resource OriginEndpoint
	err := ctx.ReadResource("aws-native:mediapackage:OriginEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OriginEndpoint resources.
type originEndpointState struct {
}

type OriginEndpointState struct {
}

func (OriginEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*originEndpointState)(nil)).Elem()
}

type originEndpointArgs struct {
	Authorization *OriginEndpointAuthorization `pulumi:"authorization"`
	// The ID of the Channel the OriginEndpoint is associated with.
	ChannelId   string                     `pulumi:"channelId"`
	CmafPackage *OriginEndpointCmafPackage `pulumi:"cmafPackage"`
	DashPackage *OriginEndpointDashPackage `pulumi:"dashPackage"`
	// A short text description of the OriginEndpoint.
	Description *string                   `pulumi:"description"`
	HlsPackage  *OriginEndpointHlsPackage `pulumi:"hlsPackage"`
	// A short string appended to the end of the OriginEndpoint URL.
	ManifestName *string                   `pulumi:"manifestName"`
	MssPackage   *OriginEndpointMssPackage `pulumi:"mssPackage"`
	// Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
	Origination *OriginEndpointOrigination `pulumi:"origination"`
	// Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
	StartoverWindowSeconds *int `pulumi:"startoverWindowSeconds"`
	// A collection of tags associated with a resource
	Tags []OriginEndpointTag `pulumi:"tags"`
	// Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
	TimeDelaySeconds *int `pulumi:"timeDelaySeconds"`
	// A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
	Whitelist []string `pulumi:"whitelist"`
}

// The set of arguments for constructing a OriginEndpoint resource.
type OriginEndpointArgs struct {
	Authorization OriginEndpointAuthorizationPtrInput
	// The ID of the Channel the OriginEndpoint is associated with.
	ChannelId   pulumi.StringInput
	CmafPackage OriginEndpointCmafPackagePtrInput
	DashPackage OriginEndpointDashPackagePtrInput
	// A short text description of the OriginEndpoint.
	Description pulumi.StringPtrInput
	HlsPackage  OriginEndpointHlsPackagePtrInput
	// A short string appended to the end of the OriginEndpoint URL.
	ManifestName pulumi.StringPtrInput
	MssPackage   OriginEndpointMssPackagePtrInput
	// Control whether origination of video is allowed for this OriginEndpoint. If set to ALLOW, the OriginEndpoint may by requested, pursuant to any other form of access control. If set to DENY, the OriginEndpoint may not be requested. This can be helpful for Live to VOD harvesting, or for temporarily disabling origination
	Origination OriginEndpointOriginationPtrInput
	// Maximum duration (seconds) of content to retain for startover playback. If not specified, startover playback will be disabled for the OriginEndpoint.
	StartoverWindowSeconds pulumi.IntPtrInput
	// A collection of tags associated with a resource
	Tags OriginEndpointTagArrayInput
	// Amount of delay (seconds) to enforce on the playback of live content. If not specified, there will be no time delay in effect for the OriginEndpoint.
	TimeDelaySeconds pulumi.IntPtrInput
	// A list of source IP CIDR blocks that will be allowed to access the OriginEndpoint.
	Whitelist pulumi.StringArrayInput
}

func (OriginEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*originEndpointArgs)(nil)).Elem()
}

type OriginEndpointInput interface {
	pulumi.Input

	ToOriginEndpointOutput() OriginEndpointOutput
	ToOriginEndpointOutputWithContext(ctx context.Context) OriginEndpointOutput
}

func (*OriginEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((*OriginEndpoint)(nil))
}

func (i *OriginEndpoint) ToOriginEndpointOutput() OriginEndpointOutput {
	return i.ToOriginEndpointOutputWithContext(context.Background())
}

func (i *OriginEndpoint) ToOriginEndpointOutputWithContext(ctx context.Context) OriginEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OriginEndpointOutput)
}

type OriginEndpointOutput struct{ *pulumi.OutputState }

func (OriginEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OriginEndpoint)(nil))
}

func (o OriginEndpointOutput) ToOriginEndpointOutput() OriginEndpointOutput {
	return o
}

func (o OriginEndpointOutput) ToOriginEndpointOutputWithContext(ctx context.Context) OriginEndpointOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(OriginEndpointOutput{})
}
