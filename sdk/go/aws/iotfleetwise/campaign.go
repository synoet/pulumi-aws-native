// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotfleetwise

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::IoTFleetWise::Campaign Resource Type
//
// Deprecated: Campaign is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Campaign struct {
	pulumi.CustomResourceState

	Action                        CampaignUpdateCampaignActionOutput   `pulumi:"action"`
	Arn                           pulumi.StringOutput                  `pulumi:"arn"`
	CollectionScheme              pulumi.AnyOutput                     `pulumi:"collectionScheme"`
	Compression                   CampaignCompressionPtrOutput         `pulumi:"compression"`
	CreationTime                  pulumi.StringOutput                  `pulumi:"creationTime"`
	DataDestinationConfigs        pulumi.ArrayOutput                   `pulumi:"dataDestinationConfigs"`
	DataExtraDimensions           pulumi.StringArrayOutput             `pulumi:"dataExtraDimensions"`
	Description                   pulumi.StringPtrOutput               `pulumi:"description"`
	DiagnosticsMode               CampaignDiagnosticsModePtrOutput     `pulumi:"diagnosticsMode"`
	ExpiryTime                    pulumi.StringPtrOutput               `pulumi:"expiryTime"`
	LastModificationTime          pulumi.StringOutput                  `pulumi:"lastModificationTime"`
	Name                          pulumi.StringOutput                  `pulumi:"name"`
	PostTriggerCollectionDuration pulumi.Float64PtrOutput              `pulumi:"postTriggerCollectionDuration"`
	Priority                      pulumi.IntPtrOutput                  `pulumi:"priority"`
	SignalCatalogArn              pulumi.StringOutput                  `pulumi:"signalCatalogArn"`
	SignalsToCollect              CampaignSignalInformationArrayOutput `pulumi:"signalsToCollect"`
	SpoolingMode                  CampaignSpoolingModePtrOutput        `pulumi:"spoolingMode"`
	StartTime                     pulumi.StringPtrOutput               `pulumi:"startTime"`
	Status                        CampaignStatusOutput                 `pulumi:"status"`
	Tags                          CampaignTagArrayOutput               `pulumi:"tags"`
	TargetArn                     pulumi.StringOutput                  `pulumi:"targetArn"`
}

// NewCampaign registers a new resource with the given unique name, arguments, and options.
func NewCampaign(ctx *pulumi.Context,
	name string, args *CampaignArgs, opts ...pulumi.ResourceOption) (*Campaign, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Action == nil {
		return nil, errors.New("invalid value for required argument 'Action'")
	}
	if args.CollectionScheme == nil {
		return nil, errors.New("invalid value for required argument 'CollectionScheme'")
	}
	if args.SignalCatalogArn == nil {
		return nil, errors.New("invalid value for required argument 'SignalCatalogArn'")
	}
	if args.TargetArn == nil {
		return nil, errors.New("invalid value for required argument 'TargetArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"collectionScheme",
		"compression",
		"diagnosticsMode",
		"expiryTime",
		"name",
		"postTriggerCollectionDuration",
		"priority",
		"signalCatalogArn",
		"spoolingMode",
		"startTime",
		"targetArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Campaign
	err := ctx.RegisterResource("aws-native:iotfleetwise:Campaign", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCampaign gets an existing Campaign resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCampaign(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CampaignState, opts ...pulumi.ResourceOption) (*Campaign, error) {
	var resource Campaign
	err := ctx.ReadResource("aws-native:iotfleetwise:Campaign", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Campaign resources.
type campaignState struct {
}

type CampaignState struct {
}

func (CampaignState) ElementType() reflect.Type {
	return reflect.TypeOf((*campaignState)(nil)).Elem()
}

type campaignArgs struct {
	Action                        CampaignUpdateCampaignAction `pulumi:"action"`
	CollectionScheme              interface{}                  `pulumi:"collectionScheme"`
	Compression                   *CampaignCompression         `pulumi:"compression"`
	DataDestinationConfigs        []interface{}                `pulumi:"dataDestinationConfigs"`
	DataExtraDimensions           []string                     `pulumi:"dataExtraDimensions"`
	Description                   *string                      `pulumi:"description"`
	DiagnosticsMode               *CampaignDiagnosticsMode     `pulumi:"diagnosticsMode"`
	ExpiryTime                    *string                      `pulumi:"expiryTime"`
	Name                          *string                      `pulumi:"name"`
	PostTriggerCollectionDuration *float64                     `pulumi:"postTriggerCollectionDuration"`
	Priority                      *int                         `pulumi:"priority"`
	SignalCatalogArn              string                       `pulumi:"signalCatalogArn"`
	SignalsToCollect              []CampaignSignalInformation  `pulumi:"signalsToCollect"`
	SpoolingMode                  *CampaignSpoolingMode        `pulumi:"spoolingMode"`
	StartTime                     *string                      `pulumi:"startTime"`
	Tags                          []CampaignTag                `pulumi:"tags"`
	TargetArn                     string                       `pulumi:"targetArn"`
}

// The set of arguments for constructing a Campaign resource.
type CampaignArgs struct {
	Action                        CampaignUpdateCampaignActionInput
	CollectionScheme              pulumi.Input
	Compression                   CampaignCompressionPtrInput
	DataDestinationConfigs        pulumi.ArrayInput
	DataExtraDimensions           pulumi.StringArrayInput
	Description                   pulumi.StringPtrInput
	DiagnosticsMode               CampaignDiagnosticsModePtrInput
	ExpiryTime                    pulumi.StringPtrInput
	Name                          pulumi.StringPtrInput
	PostTriggerCollectionDuration pulumi.Float64PtrInput
	Priority                      pulumi.IntPtrInput
	SignalCatalogArn              pulumi.StringInput
	SignalsToCollect              CampaignSignalInformationArrayInput
	SpoolingMode                  CampaignSpoolingModePtrInput
	StartTime                     pulumi.StringPtrInput
	Tags                          CampaignTagArrayInput
	TargetArn                     pulumi.StringInput
}

func (CampaignArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*campaignArgs)(nil)).Elem()
}

type CampaignInput interface {
	pulumi.Input

	ToCampaignOutput() CampaignOutput
	ToCampaignOutputWithContext(ctx context.Context) CampaignOutput
}

func (*Campaign) ElementType() reflect.Type {
	return reflect.TypeOf((**Campaign)(nil)).Elem()
}

func (i *Campaign) ToCampaignOutput() CampaignOutput {
	return i.ToCampaignOutputWithContext(context.Background())
}

func (i *Campaign) ToCampaignOutputWithContext(ctx context.Context) CampaignOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CampaignOutput)
}

type CampaignOutput struct{ *pulumi.OutputState }

func (CampaignOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Campaign)(nil)).Elem()
}

func (o CampaignOutput) ToCampaignOutput() CampaignOutput {
	return o
}

func (o CampaignOutput) ToCampaignOutputWithContext(ctx context.Context) CampaignOutput {
	return o
}

func (o CampaignOutput) Action() CampaignUpdateCampaignActionOutput {
	return o.ApplyT(func(v *Campaign) CampaignUpdateCampaignActionOutput { return v.Action }).(CampaignUpdateCampaignActionOutput)
}

func (o CampaignOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o CampaignOutput) CollectionScheme() pulumi.AnyOutput {
	return o.ApplyT(func(v *Campaign) pulumi.AnyOutput { return v.CollectionScheme }).(pulumi.AnyOutput)
}

func (o CampaignOutput) Compression() CampaignCompressionPtrOutput {
	return o.ApplyT(func(v *Campaign) CampaignCompressionPtrOutput { return v.Compression }).(CampaignCompressionPtrOutput)
}

func (o CampaignOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o CampaignOutput) DataDestinationConfigs() pulumi.ArrayOutput {
	return o.ApplyT(func(v *Campaign) pulumi.ArrayOutput { return v.DataDestinationConfigs }).(pulumi.ArrayOutput)
}

func (o CampaignOutput) DataExtraDimensions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringArrayOutput { return v.DataExtraDimensions }).(pulumi.StringArrayOutput)
}

func (o CampaignOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o CampaignOutput) DiagnosticsMode() CampaignDiagnosticsModePtrOutput {
	return o.ApplyT(func(v *Campaign) CampaignDiagnosticsModePtrOutput { return v.DiagnosticsMode }).(CampaignDiagnosticsModePtrOutput)
}

func (o CampaignOutput) ExpiryTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringPtrOutput { return v.ExpiryTime }).(pulumi.StringPtrOutput)
}

func (o CampaignOutput) LastModificationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.LastModificationTime }).(pulumi.StringOutput)
}

func (o CampaignOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o CampaignOutput) PostTriggerCollectionDuration() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *Campaign) pulumi.Float64PtrOutput { return v.PostTriggerCollectionDuration }).(pulumi.Float64PtrOutput)
}

func (o CampaignOutput) Priority() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Campaign) pulumi.IntPtrOutput { return v.Priority }).(pulumi.IntPtrOutput)
}

func (o CampaignOutput) SignalCatalogArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.SignalCatalogArn }).(pulumi.StringOutput)
}

func (o CampaignOutput) SignalsToCollect() CampaignSignalInformationArrayOutput {
	return o.ApplyT(func(v *Campaign) CampaignSignalInformationArrayOutput { return v.SignalsToCollect }).(CampaignSignalInformationArrayOutput)
}

func (o CampaignOutput) SpoolingMode() CampaignSpoolingModePtrOutput {
	return o.ApplyT(func(v *Campaign) CampaignSpoolingModePtrOutput { return v.SpoolingMode }).(CampaignSpoolingModePtrOutput)
}

func (o CampaignOutput) StartTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringPtrOutput { return v.StartTime }).(pulumi.StringPtrOutput)
}

func (o CampaignOutput) Status() CampaignStatusOutput {
	return o.ApplyT(func(v *Campaign) CampaignStatusOutput { return v.Status }).(CampaignStatusOutput)
}

func (o CampaignOutput) Tags() CampaignTagArrayOutput {
	return o.ApplyT(func(v *Campaign) CampaignTagArrayOutput { return v.Tags }).(CampaignTagArrayOutput)
}

func (o CampaignOutput) TargetArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Campaign) pulumi.StringOutput { return v.TargetArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CampaignInput)(nil)).Elem(), &Campaign{})
	pulumi.RegisterOutputType(CampaignOutput{})
}
